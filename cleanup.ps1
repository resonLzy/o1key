# 读取文件
$lines = Get-Content utils.py -Encoding UTF8

# 移除第 149 行的重复"正在调用 API"（如果存在）
if ($lines[148] -match '正在调用 API') {
    $lines = $lines[0..147] + $lines[149..($lines.Count-1)]
}

# 写回文件
$lines | Set-Content utils.py -Encoding UTF8
Write-Host '✅ 清理完成'
