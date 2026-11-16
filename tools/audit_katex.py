import glob
import os
import re

clases_files = sorted(glob.glob("Clases/**/*.md", recursive=True))

total_math_blocks = 0
total_inline_math = 0
syntax_errors = []

for file_path in clases_files:
    rel_path = os.path.relpath(file_path)
    with open(file_path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    in_display_math = False
    display_math_buffer = []
    display_math_start_line = 0

    for line_num, line in enumerate(lines, start=1):
        stripped = line.strip()

        # Check multi-line display math
        if stripped == "$$":
            if not in_display_math:
                in_display_math = True
                display_math_buffer = []
                display_math_start_line = line_num
            else:
                in_display_math = False
                total_math_blocks += 1
                math_content = "\n".join(display_math_buffer)
                # Check balanced braces
                if math_content.count("{") != math_content.count("}"):
                    syntax_errors.append(f"{rel_path}:{display_math_start_line}: Unbalanced braces in $$ block: {math_content.count('{')} open vs {math_content.count('}')} close")
                # Check for illegal $ inside math block
                if "$" in math_content:
                    syntax_errors.append(f"{rel_path}:{display_math_start_line}: Found inner '$' inside $$ math block: {math_content[:50]}...")
            continue

        if in_display_math:
            display_math_buffer.append(line)
            continue

        # Single-line display math: $$...$$
        if stripped.startswith("$$") and stripped.endswith("$$") and len(stripped) > 4:
            total_math_blocks += 1
            inner = stripped[2:-2].strip()
            if inner.count("{") != inner.count("}"):
                syntax_errors.append(f"{rel_path}:{line_num}: Unbalanced braces in single-line $$: {inner[:60]}")
            if "$" in inner:
                syntax_errors.append(f"{rel_path}:{line_num}: Inner '$' inside single-line $$: {inner[:60]}")
            continue

        # Inline math checks on the line
        # Split line by inline $ but ignore escaped \$
        # Note: In markdown, inline math is delimited by $...$
        # Count non-escaped $ on the line
        dollar_count = len(re.findall(r"(?<!\\)\$", line))
        if dollar_count % 2 != 0:
            # Check if this line is inside a code block
            # If odd number of $, an inline math delimiter is unclosed on this single line
            syntax_errors.append(f"{rel_path}:{line_num}: Odd number of '$' ({dollar_count}) on line: {stripped[:80]}")
        else:
            total_inline_math += dollar_count // 2
            # For each inline math block $...$, check balanced braces
            matches = re.findall(r"(?<!\\)\$(.+?)(?<!\\)\$", line)
            for m in matches:
                if m.count("{") != m.count("}"):
                    syntax_errors.append(f"{rel_path}:{line_num}: Unbalanced braces in inline math ${m[:40]}$")

print(f"=== REPORTE DE AUDITORIA RIGUROSA KATEX / LATEX ===")
print(f"Total archivos escaneados: {len(clases_files)}")
print(f"Total bloques display math ($$): {total_math_blocks}")
print(f"Total expresiones inline math ($...$): {total_inline_math}")
print(f"Total errores de sintaxis detectados: {len(syntax_errors)}")
for err in syntax_errors[:30]:
    print(f"  ❌ {err}")
if len(syntax_errors) > 30:
    print(f"  ... y {len(syntax_errors) - 30} errores más.")
