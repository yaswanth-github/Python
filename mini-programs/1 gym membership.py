import csv

class Member:
    def __init__(self, name, email, phone, membership_status):
        self.name = name
        self.email = email
        self.phone = phone
        self.membership_status = membership_status
    
class GymMembershipDatabase:
    def __init__(self, file_name):
        self.file_name = file_name
        self.members = []
    
    def load_members(self):
        with open(self.file_name, 'r') as f:
            reader = csv.reader(f)
            next(reader)  # skip header row
            for row in reader:
                name, email, phone, membership_status = row
                member = Member(name, email, phone, membership_status)
                self.members.append(member)
    
    def add_member(self, member):
        self.members.append(member)
    
    def save_members(self):
        with open(self.file_name, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['Name', 'Email', 'Phone', 'Membership Status'])
            for member in self.members:
                writer.writerow([member.name, member.email, member.phone, member.membership_status])
    
    def get_member_by_email(self, email):
        for member in self.members:
            if member.email == email:
                return member
        return None
    
    def get_members_by_membership_status(self, membership_status):
        matching_members = []
        for member in self.members:
            if member.membership_status == membership_status:
                matching_members.append(member)
        return matching_members
    
    def generate_report(self):
        active_members = self.get_members_by_membership_status('Active')
        inactive_members = self.get_members_by_membership_status('Inactive')
        print(f'Number of active members: {len(active_members)}')
        print(f'Number of inactive members: {len(inactive_members)}')
        print('Active members:')
        for member in active_members:
            print(f'- {member.name} ({member.email})')
        print('Inactive members:')
        for member in inactive_members:
            print(f'- {member.name} ({member.email})')

membership_db = GymMembershipDatabase('mini-programs/members.csv')
membership_db.load_members()

# Add a new member
new_member = Member('John Doe', 'johndoe@example.com', '555-1234', 'Active')
membership_db.add_member(new_member)

# Update a member's membership status
existing_member = membership_db.get_member_by_email('janedoe@example.com')
existing_member.membership_status = 'Inactive'

# Save changes to the file
membership_db.save_members()

# Generate a report
membership_db.generate_report()
