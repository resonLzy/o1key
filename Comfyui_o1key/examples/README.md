# Example Workflows for Comfyui_o1key

This directory contains example workflow JSON files that demonstrate how to use the Nano Banana nodes.

## Available Workflows

### 1. text_to_image_basic.json
Basic text-to-image generation workflow showing:
- Simple prompt setup
- Default settings (1:1 aspect ratio, b64_json format)
- Direct connection to preview node

### 2. text_to_image_advanced.json
Advanced text-to-image workflow demonstrating:
- Multiple aspect ratios
- Different image sizes (1K, 2K, 4K)
- URL vs Base64 response format comparison
- Saving output to file

### 3. image_to_image_basic.json
Basic image-to-image transformation workflow:
- Loading a reference image
- Applying style transfer via prompt
- Preserving composition while changing style

### 4. image_to_image_advanced.json
Advanced image-to-image workflow showing:
- Multiple transformations in sequence
- Comparing different aspect ratios
- Batch processing setup

## How to Use

1. Open ComfyUI
2. Click "Load" in the menu
3. Navigate to this `examples` folder
4. Select a workflow JSON file
5. Update the `api_key` parameter in the Nano Banana nodes
6. Click "Queue Prompt" to run

## Notes

- Make sure to set your actual API key before running workflows
- Workflows assume default ComfyUI nodes are available
- You can customize prompts, aspect ratios, and other parameters as needed
- Start with basic workflows if you're new to the plugin
