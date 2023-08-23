def main():
    filename = input("Input the Filename: ")
    extensions = {
        'py': 'python',
    }

    parts = filename.split('.')
    if len(parts) > 1:
        extension = parts[-1]
        if extension in extensions:
            description = extensions[extension]
            print(f"The extension of the file is: '{description}'")

if __name__ == "__main__":
    main()
