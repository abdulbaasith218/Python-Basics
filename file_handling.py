
#Modes (One-Liner Summary):

#   Mode                Description
#   'r'            Read-only (file must exist)
#   'w'            Write-only (overwrites or creates)
#   'a'            Append-only (adds to end of file)
#   'r+'              Read + write (file must exist)
#   'w+'            Write + read (overwrites or creates)
#   'a+'           Append + read (creates if not exists)
#   'rb'             Read binary
#   'wb'             Write binary
#   'ab'           Append binary


#write
file = open("notes.txt", "w")
file.write("Welcome to Python File Handling!\n")
file.write("This is a new file.\n")
file.close()









