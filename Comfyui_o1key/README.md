# Comfyui_o1key

[English](#english) | [中文](#中文)

---

## English

ComfyUI plugin for Nano Banana image generation API, providing text-to-image and image-to-image capabilities.

### Features

🎨 **Dual Generation Modes**
- Text-to-Image: Generate images from text prompts
- Image-to-Image: Transform existing images with text guidance

🚀 **Advanced Features**
- Two model options: `nano-banana-pro-svip` (recommended) and `nano-banana-svip`
- 10 aspect ratios: 1:1, 4:3, 3:4, 16:9, 9:16, 2:3, 3:2, 4:5, 5:4, 21:9
- Image size control: 1K, 2K, 4K (Pro model only)
- Flexible response formats: URL or Base64 JSON
- Automatic retry with exponential backoff (3 attempts)
- Comprehensive error handling
- No charge on failure guarantee

### Installation

1. Navigate to your ComfyUI custom nodes directory:
```bash
cd ComfyUI/custom_nodes/
```

2. Clone this repository:
```bash
git clone https://github.com/yourusername/Comfyui_o1key.git
```

3. Install required dependencies:
```bash
cd Comfyui_o1key
pip install -r requirements.txt
```

4. Restart ComfyUI

### Usage

#### 1. Text-to-Image Generation

1. Add the **Nano Banana Text-to-Image** node to your workflow
2. Configure parameters:
   - **Prompt**: Your text description
   - **API Key**: Your o1key.com API key
   - **Model**: Choose between `nano-banana-pro-svip` (default) or `nano-banana-svip`
   - **Aspect Ratio**: Select desired aspect ratio
   - **Response Format**: Choose `b64_json` (faster) or `url`
   - **Image Size**: 1K/2K/4K (Pro model only)
3. Connect to preview or save nodes
4. Run the workflow

#### 2. Image-to-Image Generation

1. Add the **Nano Banana Image-to-Image** node
2. Connect a reference image to the `image` input
3. Configure same parameters as text-to-image
4. The node will use your reference image to guide generation
5. Run the workflow

### Getting Your API Key

1. Visit [o1key.com](https://o1key.com)
2. Sign up or log in to your account
3. Navigate to API settings
4. Create a new API key from Google AI Studio
5. Copy the key and use it in the plugin

### Parameters

| Parameter | Description | Options |
|-----------|-------------|---------|
| `prompt` | Text description of desired image | Any string |
| `api_key` | Your o1key.com API key | String |
| `model` | Generation model | `nano-banana-pro-svip`, `nano-banana-svip` |
| `aspect_ratio` | Image aspect ratio | 1:1, 4:3, 3:4, 16:9, 9:16, 2:3, 3:2, 4:5, 5:4, 21:9 |
| `response_format` | API response format | `url`, `b64_json` |
| `image_size` | Output image resolution | `1K`, `2K`, `4K` (Pro model only) |
| `image` (I2I only) | Reference image | ComfyUI IMAGE tensor |

### Model Comparison

| Feature | nano-banana-svip | nano-banana-pro-svip |
|---------|------------------|----------------------|
| Speed | Fast | Fast |
| Quality | High | Very High |
| Image Sizes | 1K, 2K | 1K, 2K, 4K |
| Recommended | ✓ | ✓✓ (Default) |

### Troubleshooting

**Problem: "API key is required" error**
- Solution: Make sure you've entered your API key in the node parameters

**Problem: "API error (status 401)" error**
- Solution: Check that your API key is valid and hasn't expired

**Problem: Image generation fails without clear error**
- Solution: Check your internet connection and API service status at o1key.com

**Problem: Node doesn't appear in ComfyUI**
- Solution: Ensure you've installed dependencies and restarted ComfyUI completely

### Technical Details

- **API Endpoint**: `https://o1key.com/v1/images/generations`
- **Authentication**: Bearer token via Authorization header
- **Retry Logic**: 3 attempts with exponential backoff (1s, 2s, 4s)
- **Timeout**: 60 seconds per request
- **Supported Image Formats**: PNG, JPEG (auto-converted to RGB)

### Error Handling

The plugin implements robust error handling:
- **Network errors**: Automatic retry with exponential backoff
- **API errors**: Clear error messages with status codes
- **Invalid responses**: Proper validation and user feedback
- **Failed requests**: No charges (as per platform policy)

### License

MIT License - See LICENSE file for details

### Support

- Issues: [GitHub Issues](https://github.com/yourusername/Comfyui_o1key/issues)
- Website: [o1key.com](https://o1key.com)

---

## 中文

ComfyUI 插件，集成 Nano Banana 图像生成 API，提供文生图和图生图功能。

### 功能特性

🎨 **双生成模式**
- 文生图：从文本提示生成图像
- 图生图：使用文本引导转换现有图像

🚀 **高级功能**
- 两种模型选择：`nano-banana-pro-svip`（推荐）和 `nano-banana-svip`
- 10种宽高比：1:1, 4:3, 3:4, 16:9, 9:16, 2:3, 3:2, 4:5, 5:4, 21:9
- 图像尺寸控制：1K、2K、4K（仅Pro模型）
- 灵活的响应格式：URL 或 Base64 JSON
- 自动重试机制（指数退避，3次尝试）
- 完善的错误处理
- 失败不扣费保障

### 安装方法

1. 进入 ComfyUI 的 custom_nodes 目录：
```bash
cd ComfyUI/custom_nodes/
```

2. 克隆此仓库：
```bash
git clone https://github.com/yourusername/Comfyui_o1key.git
```

3. 安装依赖：
```bash
cd Comfyui_o1key
pip install -r requirements.txt
```

4. 重启 ComfyUI

### 使用说明

#### 1. 文生图

1. 添加 **Nano Banana Text-to-Image** 节点到工作流
2. 配置参数：
   - **Prompt**：文本描述
   - **API Key**：您的 o1key.com API 密钥
   - **Model**：选择 `nano-banana-pro-svip`（默认）或 `nano-banana-svip`
   - **Aspect Ratio**：选择所需宽高比
   - **Response Format**：选择 `b64_json`（更快）或 `url`
   - **Image Size**：1K/2K/4K（仅Pro模型）
3. 连接到预览或保存节点
4. 运行工作流

#### 2. 图生图

1. 添加 **Nano Banana Image-to-Image** 节点
2. 将参考图像连接到 `image` 输入
3. 配置与文生图相同的参数
4. 节点将使用参考图像引导生成
5. 运行工作流

### 获取 API 密钥

1. 访问 [o1key.com](https://o1key.com)
2. 注册或登录账户
3. 进入 API 设置
4. 从 Google AI Studio 创建新的 API 密钥
5. 复制密钥并在插件中使用

### 参数说明

| 参数 | 说明 | 选项 |
|------|------|------|
| `prompt` | 图像的文本描述 | 任意字符串 |
| `api_key` | o1key.com API 密钥 | 字符串 |
| `model` | 生成模型 | `nano-banana-pro-svip`, `nano-banana-svip` |
| `aspect_ratio` | 图像宽高比 | 1:1, 4:3, 3:4, 16:9, 9:16, 2:3, 3:2, 4:5, 5:4, 21:9 |
| `response_format` | API 响应格式 | `url`, `b64_json` |
| `image_size` | 输出图像分辨率 | `1K`, `2K`, `4K`（仅Pro模型）|
| `image`（仅图生图）| 参考图像 | ComfyUI IMAGE 张量 |

### 模型对比

| 特性 | nano-banana-svip | nano-banana-pro-svip |
|------|------------------|----------------------|
| 速度 | 快 | 快 |
| 质量 | 高 | 非常高 |
| 图像尺寸 | 1K, 2K | 1K, 2K, 4K |
| 推荐度 | ✓ | ✓✓（默认）|

### 常见问题

**问题："API key is required" 错误**
- 解决：确保在节点参数中输入了 API 密钥

**问题："API error (status 401)" 错误**
- 解决：检查 API 密钥是否有效且未过期

**问题：图像生成失败且无明确错误**
- 解决：检查网络连接和 o1key.com 的 API 服务状态

**问题：节点未在 ComfyUI 中显示**
- 解决：确保已安装依赖并完全重启 ComfyUI

### 技术细节

- **API 端点**：`https://o1key.com/v1/images/generations`
- **认证方式**：通过 Authorization header 的 Bearer token
- **重试逻辑**：3次尝试，指数退避（1秒、2秒、4秒）
- **超时设置**：每个请求 60 秒
- **支持的图像格式**：PNG、JPEG（自动转换为 RGB）

### 错误处理

插件实现了完善的错误处理：
- **网络错误**：自动重试，指数退避
- **API错误**：清晰的错误消息和状态码
- **无效响应**：适当的验证和用户反馈
- **失败请求**：不收费（依据平台政策）

### 许可证

MIT License - 详见 LICENSE 文件

### 支持

- 问题反馈：[GitHub Issues](https://github.com/yourusername/Comfyui_o1key/issues)
- 官网：[o1key.com](https://o1key.com)
