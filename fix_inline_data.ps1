# 读取文件
$lines = Get-Content utils.py -Encoding UTF8

# 找到需要替换的代码块（大约在第 275-283 行）
$startLine = -1
$endLine = -1

for ($i = 0; $i -lt $lines.Count; $i++) {
    if ($lines[$i] -match "# Try to find inline_data.*first" -and $i -gt 270) {
        $startLine = $i
    }
    if ($startLine -gt 0 -and $lines[$i] -match "return decode_base64_image\(base64_data\)" -and $i -lt 290) {
        $endLine = $i
        break
    }
}

if ($startLine -gt 0 -and $endLine -gt 0) {
    Write-Host "找到替换区域: 第 $($startLine+1) 行到第 $($endLine+1) 行"
    
    # 新的代码块
    $newCode = @"
        # Try to find inline_data (official Gemini format) first
        for part in parts:
            if 'inline_data' in part:
                inline_data = part['inline_data']
                
                # 处理两种格式：
                # 1. 标准格式: {"mime_type": "...", "data": "base64..."}
                # 2. SVIP格式: 直接是 base64 字符串
                if isinstance(inline_data, dict):
                    # 标准 Gemini 格式
                    base64_data = inline_data.get('data')
                    if base64_data:
                        logger.debug("Found inline_data (standard Gemini format with dict)")
                        return decode_base64_image(base64_data)
                elif isinstance(inline_data, str):
                    # SVIP 格式：直接是 base64 字符串
                    logger.debug("Found inline_data (SVIP format with direct base64 string)")
                    return decode_base64_image(inline_data)
"@
    
    # 构建新的文件内容
    $newLines = @()
    for ($i = 0; $i -lt $lines.Count; $i++) {
        if ($i -eq $startLine) {
            $newLines += $newCode
            # 跳过原来的代码块
            $i = $endLine
        } elseif ($i -ne $endLine) {
            $newLines += $lines[$i]
        }
    }
    
    # 写回文件
    $newLines | Set-Content utils.py -Encoding UTF8
    Write-Host "✅ 代码已成功修改"
} else {
    Write-Host "❌ 未找到替换区域"
    Write-Host "startLine: $startLine, endLine: $endLine"
}
