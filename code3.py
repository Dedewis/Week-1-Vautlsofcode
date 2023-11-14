def read_and_write_file(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
        with open(filename, 'w') as file:
            file.write(content.upper())
        print(f"File'{filename}' processed successfully.")
    except Exception as e:
        print(f"An error occured :{str(e)}")
def main():
    filename = "sample.txt"
    read_and_write_file(filename)
if __name__ =="__main__":
 main()