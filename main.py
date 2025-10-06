# Import needed package
import pycodestyle

# Create a StyleGuide instance
style_checker = pycodestyle.StyleGuide()

# Run PEP 8 check on multiple files
result = style_checker.check_files(['main.py'])

# Print result of PEP 8 style check
print(result.messages)

def main():
    print("Hello from py-dc!")


if __name__ == "__main__":
    main()
