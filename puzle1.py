def escape_for_js(code):
    return (code
            .replace("\\", "\\\\")
            .replace("`", "\\`")
            .replace('"', '\\"')
            .replace("{", "{{")
            .replace("}", "}}"))

python_code = '''
def main():
    python_code = \"\"\"{0}\"\"\"
    js_code = f"console.log(`{1}`)"
    print(js_code)

if __name__ == "__main__":
    main()
'''

escaped_python_code = escape_for_js(python_code)
js_code = f'console.log(`{escaped_python_code}`);'

print(js_code)
