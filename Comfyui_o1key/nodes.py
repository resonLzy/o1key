"""
ComfyUI nodes for Nano Banana image generation
"""
from .utils import (
    call_nano_banana_api,
    process_api_response,
    pil_to_comfy_image,
    comfy_image_to_base64
)
import logging

logger = logging.getLogger(__name__)


class NanoBananaTextToImage:
    """
    ComfyUI node for text-to-image generation using Nano Banana API
    """
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {
                    "multiline": True,
                    "default": "a beautiful sunset over mountains"
                }),
                "api_key": ("STRING", {
                    "multiline": False,
                    "default": ""
                }),
                "model": (["nano-banana-pro-svip", "nano-banana-svip"], {
                    "default": "nano-banana-pro-svip"
                }),
                "aspect_ratio": ([
                    "1:1", "4:3", "3:4", "16:9", "9:16", 
                    "2:3", "3:2", "4:5", "5:4", "21:9"
                ], {
                    "default": "1:1"
                }),
            },
            "optional": {
                "seed": ("INT", {
                    "default": -1,
                    "min": -1,
                    "max": 2147483647,
                    "display": "number"
                }),
                "image_size": (["1K", "2K", "4K"], {
                    "default": "2K"
                }),
            }
        }
    
    RETURN_TYPES = ("IMAGE",)
    RETURN_NAMES = ("image",)
    FUNCTION = "generate_image"
    CATEGORY = "o1key"
    
    def generate_image(self, prompt, api_key, model, aspect_ratio, seed=-1, image_size="2K"):
        """
        Generate image from text prompt
        """
        try:
            print(f"\n{'='*60}")
            print(f"🎨 Nano Banana 文生图")
            print(f"{'='*60}")
            print(f"提示词: {prompt[:80]}{'...' if len(prompt) > 80 else ''}")
            print(f"模型: {model}")
            print(f"宽高比: {aspect_ratio}")
            if seed >= 0:
                print(f"种子: {seed}")
            print(f"{'='*60}\n")
            
            logger.debug(f"Full params - Model: {model}, Aspect: {aspect_ratio}, Size: {image_size}")
            
            # Only use image_size for nano-banana-pro-svip
            size_param = image_size if model == "nano-banana-pro-svip" else None
            
            # Process seed (-1 means random)
            seed_param = None if seed < 0 else seed
            
            # Call API
            response_data = call_nano_banana_api(
                prompt=prompt,
                model=model,
                aspect_ratio=aspect_ratio,
                image_size=size_param,
                seed=seed_param,
                api_key=api_key
            )
            
            # Process response
            pil_image = process_api_response(response_data)
            
            # Convert to ComfyUI format
            comfy_image = pil_to_comfy_image(pil_image)
            
            print(f"\n✅ 图片生成完成!\n")
            return (comfy_image,)
            
        except Exception as e:
            error_msg = f"❌ 文生图失败: {str(e)}"
            print(f"\n{error_msg}\n")
            logger.error(error_msg)
            raise Exception(error_msg)


class NanoBananaImageToImage:
    """
    ComfyUI node for image-to-image generation using Nano Banana API
    """
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "image": ("IMAGE",),
                "prompt": ("STRING", {
                    "multiline": True,
                    "default": "transform this into a watercolor painting"
                }),
                "api_key": ("STRING", {
                    "multiline": False,
                    "default": ""
                }),
                "model": (["nano-banana-pro-svip", "nano-banana-svip"], {
                    "default": "nano-banana-pro-svip"
                }),
                "aspect_ratio": ([
                    "1:1", "4:3", "3:4", "16:9", "9:16", 
                    "2:3", "3:2", "4:5", "5:4", "21:9"
                ], {
                    "default": "1:1"
                }),
            },
            "optional": {
                "seed": ("INT", {
                    "default": -1,
                    "min": -1,
                    "max": 2147483647,
                    "display": "number"
                }),
                "image_size": (["1K", "2K", "4K"], {
                    "default": "2K"
                }),
            }
        }
    
    RETURN_TYPES = ("IMAGE",)
    RETURN_NAMES = ("image",)
    FUNCTION = "generate_image"
    CATEGORY = "o1key"
    
    def generate_image(self, image, prompt, api_key, model, aspect_ratio, seed=-1, image_size="2K"):
        """
        Generate image from reference image and text prompt
        """
        try:
            print(f"\n{'='*60}")
            print(f"🎨 Nano Banana 图生图")
            print(f"{'='*60}")
            print(f"提示词: {prompt[:80]}{'...' if len(prompt) > 80 else ''}")
            print(f"模型: {model}")
            print(f"宽高比: {aspect_ratio}")
            if seed >= 0:
                print(f"种子: {seed}")
            print(f"参考图: {image.shape[2]}x{image.shape[1]}")
            print(f"{'='*60}\n")
            
            logger.debug(f"Reference image shape: {image.shape}")
            
            # Convert reference image to base64
            reference_base64 = comfy_image_to_base64(image)
            
            # Only use image_size for nano-banana-pro-svip
            size_param = image_size if model == "nano-banana-pro-svip" else None
            
            # Process seed (-1 means random)
            seed_param = None if seed < 0 else seed
            
            # Call API
            response_data = call_nano_banana_api(
                prompt=prompt,
                model=model,
                aspect_ratio=aspect_ratio,
                image_size=size_param,
                seed=seed_param,
                api_key=api_key,
                reference_image_base64=reference_base64
            )
            
            # Process response
            pil_image = process_api_response(response_data)
            
            # Convert to ComfyUI format
            comfy_image = pil_to_comfy_image(pil_image)
            
            print(f"\n✅ 图片生成完成!\n")
            return (comfy_image,)
            
        except Exception as e:
            error_msg = f"❌ 图生图失败: {str(e)}"
            print(f"\n{error_msg}\n")
            logger.error(error_msg)
            raise Exception(error_msg)


# Node class mappings for ComfyUI
NODE_CLASS_MAPPINGS = {
    "NanoBananaTextToImage": NanoBananaTextToImage,
    "NanoBananaImageToImage": NanoBananaImageToImage,
}

# Node display names in ComfyUI interface
NODE_DISPLAY_NAME_MAPPINGS = {
    "NanoBananaTextToImage": "Nano Banana Text-to-Image",
    "NanoBananaImageToImage": "Nano Banana Image-to-Image",
}
