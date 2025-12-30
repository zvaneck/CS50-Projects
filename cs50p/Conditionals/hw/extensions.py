file_name = input("Input file name: ")
dot_count = file_name.count(".")

if "." in file_name:
    file_type = file_name.replace(" ", "").casefold().split(".")[dot_count]
    match file_type:
        case "gif" | "png":
            print(f"image/{file_type}")
        case "jpg" | "jpeg":
            print("image/jpeg")
        case "pdf" | "zip":
            print(f"application/{file_type}")
        case "txt":
            print("text/plain")
        case _:
            print("application/octet-stream")
else:
    print("application/octet-stream")

#print(file_name.split(".")[1])