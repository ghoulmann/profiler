#!/home/RikGoldman/.virtualenvs/profiler/bin/python
"""
Creates a random human profile with personal data
"""
from profiler import Person
def main():
    """
    Create a fake profile, print it, delete it
    """
    a_profile = Person()
    a_profile.__str__()
    del a_profile
if __name__ == "__main__":
    main()
