import subprocess

def main():
  scriptPath = 'stager.py'
  command = ['python', scriptPath]
  subprocess.run(command)
  print("Stager has finished.")

  scriptPath = 'mailman.py'
  command = ['python', scriptPath]
  subprocess.run(command)
  print("Mailman has finished.")


if __name__ == "__main__":
    main()
