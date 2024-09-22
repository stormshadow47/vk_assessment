import csv
import re


def validate_email(email):
  email_regex = r"^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,4})+$"
  return re.match(email_regex, email) is not None

def clean_csv(input_file, output_file):

  seen_ids = set()
  with open(input_file, 'r', newline='') as infile, open(output_file, 'w', newline='') as outfile:
    reader = csv.DictReader(infile)
    writer = csv.DictWriter(outfile, fieldnames=reader.fieldnames)
    writer.writeheader()

    for row in reader:
      user_id = row['user_id']
      email = row['email']

      if user_id not in seen_ids and validate_email(email):
        seen_ids.add(user_id)
        writer.writerow(row)

if __name__ == "__main__":
  input_file = "D:\input.csv" 
  output_file = "cleaned.csv" 
  clean_csv(input_file, output_file)