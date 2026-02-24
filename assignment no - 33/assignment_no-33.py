import psutil
import sys
import os
import time
import schedule



def CreateLog(FolderName):

    Border = "-" * 50
    print(Border)

    if not os.path.exists(FolderName):
        os.mkdir(FolderName)
        print("Directory created successfully")

    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
    FileName = os.path.join(FolderName, "Marvellous_%s.log" % timestamp)

    print("Log file created:", FileName)

    fobj = open(FileName, "w")

    fobj.write(Border + "\n")
    fobj.write("------Marvellous Platform Surveillance System-----\n")
    fobj.write("Log created at : " + time.ctime() + "\n")
    fobj.write(Border + "\n\n")

    

    fobj.write("CPU Usage : %s %%\n" % psutil.cpu_percent())
    fobj.write("RAM Usage : %s %%\n" % psutil.virtual_memory().percent)
    fobj.write(Border + "\n")

    

    Data = ProcessScan()

    fobj.write("\nTop 10 Memory Consuming Processes\n")
    fobj.write(Border + "\n")

   
    sorted_data = sorted(Data, key=lambda x: x["memory_percent"], reverse=True)

    count = 0
    for proc in sorted_data:
        if count == 10:
            break
        fobj.write(proc["name"] + " -> " +
                   str(round(proc["memory_percent"], 2)) + " %\n")
        count = count + 1

    fobj.write(Border + "\n\n")

    
    for info in Data:

        fobj.write("PID: %s\n" % info.get("pid"))
        fobj.write("Name: %s\n" % info.get("name"))
        fobj.write("Username: %s\n" % info.get("username"))
        fobj.write("Status: %s\n" % info.get("status"))
        fobj.write("Start Time: %s\n" % info.get("create_time"))
        fobj.write("CPU %%: %.2f\n" % info.get("cpu_percent"))
        fobj.write("Memory %%: %.2f\n" % info.get("memory_percent"))

        
        fobj.write("RSS (Actual Memory): %s bytes\n" % info.get("rss"))
        fobj.write("VMS (Virtual Memory): %s bytes\n" % info.get("vms"))
        fobj.write("Thread Count: %s\n" % info.get("threads"))
        fobj.write("Open Files: %s\n" % info.get("open_files"))

        fobj.write(Border + "\n")


    fobj.write("\nSUMMARY\n")
    fobj.write("Total Processes: %s\n" % len(Data))

    if len(sorted_data) > 0:
        fobj.write("Top Memory Process: %s\n" % sorted_data[0]["name"])

    fobj.write(Border + "\n")
    fobj.write("End of Log File\n")
    fobj.write(Border + "\n")

    fobj.close()

def ProcessScan():

    listprocess = []

    # Warm up CPU %
    for proc in psutil.process_iter():
        try:
            proc.cpu_percent()
        except:
            pass

    time.sleep(0.2)

    for proc in psutil.process_iter():

        try:
            info = {}

            info["pid"] = proc.pid
            info["name"] = proc.name()
            info["username"] = proc.username()
            info["status"] = proc.status()

            try:
                info["create_time"] = time.strftime(
                    "%Y-%m-%d %H:%M:%S",
                    time.localtime(proc.create_time()))
            except:
                info["create_time"] = "NA"

            info["cpu_percent"] = proc.cpu_percent()
            info["memory_percent"] = proc.memory_percent()

            mem = proc.memory_info()
            info["rss"] = mem.rss
            info["vms"] = mem.vms

            info["threads"] = proc.num_threads()

            try:
                info["open_files"] = len(proc.open_files())
            except:
                info["open_files"] = "Access Denied"

            listprocess.append(info)

        except:
            pass

    return listprocess

def main():

    Border = "-" * 50
    print(Border)
    print("------Marvellous Platform Surveillance System-----")
    print(Border)

    if (len(sys.argv) == 2):

        if (sys.argv[1] == "--h" or sys.argv[1] == "--H"):
            print("This script creates automatic system logs.")
            print("Added features:")
            print("This is script is used to : ") 
            print("1 : Create automatic logs") 
            print("2 : Executes periodically") 
            print("3 : Sends mail with the log ") 
            print("4 : Store information about processes") 
            print("5 : Store information about CPU") 
            print("6 : Store information about RAM usage ") 
            print("7: Store information about secondary storage(harddisk)")
            print("8. Thread Monitoring")
            print("9. Open Files Monitoring")
            print("10. RSS and VMS Memory")
            print("11. Top 10 Memory Processes")


        elif (sys.argv[1] == "--u" or sys.argv[1] == "--U"):
            print("Use as:")
            print("ScriptName.py TimeInterval DirectoryName")

        else:
            print("Invalid option")

    elif (len(sys.argv) == 3):

        schedule.every(int(sys.argv[1])).minutes.do(CreateLog, sys.argv[2])

        print("Platform Surveillance System started")
        print("Press Ctrl + C to stop")

        while True:
            schedule.run_pending()
            time.sleep(1)

    else:
        print("Invalid number of arguments")


if __name__ == "__main__":
    main()