"""
## 4. Counter Class with Class vs Instance Attributes  *(Medium)*

=================================================
COUNTER WITH CLASS VS INSTANCE ATTRIBUTES
=================================================

Problem Statement:
Write a Python CLASS called `Counter` that
maintains:
   - an INSTANCE counter for the current
     object (its own count)
   - a CLASS counter shared across ALL objects
     (the total count across the program)

The goal of this problem is to understand the
difference between:
   - INSTANCE attributes  (one per object,
     stored on `self`)
   - CLASS attributes     (one for the whole
     class, stored on the class itself)

-------------------------------------------------
Instructions:
1. Define the class:
      class Counter:
          total = 0       # CLASS attribute

          def __init__(self, name):
              self.name  = name
              self.count = 0   # INSTANCE attribute
2. Instance methods:
      - increment(self, step=1)
            * self.count  += step
            * Counter.total += step
        (note: use Counter.total, NOT self.total,
         when UPDATING the class attribute)
      - reset(self)
            * sets self.count back to 0
            * does NOT touch Counter.total
      - __str__(self)
            * "<name>: count=<count>"
3. Class method (regular method that touches
   class attribute):
      - show_total() can be a @staticmethod or
        a regular function inside the class
        that returns Counter.total
4. In the driver code:
      - create at least THREE Counter objects
      - call increment() a different number of
        times on each
      - reset ONE of them
      - print each object using print(c)
      - print the overall Counter.total
5. Do NOT use:
   - the global keyword
   - any external library

-------------------------------------------------
Input Example:
c1 = Counter("clicks")
c2 = Counter("views")
c3 = Counter("downloads")

for _ in range(3):
    c1.increment()
for _ in range(5):
    c2.increment()
c3.increment(10)
c1.reset()

Output Example:
clicks:    count=0
views:     count=5
downloads: count=10
Total across all counters: 18

-------------------------------------------------
Explanation:
- `c1.count`, `c2.count`, and `c3.count` are
  three SEPARATE numbers, because each lives
  on its own object.
- `Counter.total` is a SINGLE number shared by
  the whole class. Every increment() call adds
  to it, including the ones that were later
  reset on the instance.
- This is why c1 shows 0 but the class total
  is still 18 (3 + 5 + 10).
=================================================

"""
class Counter:
    # CLASS attribute shared across all objects
    total = 0 

    def __init__(self, name):
        # INSTANCE attributes unique to each object
        self.name = name
        self.count = 0 

    def increment(self, step=1):
        # Update instance attribute
        self.count += step
        # Update class attribute
        Counter.total += step

    def reset(self):
        # Sets instance count back to 0 without touching Counter.total
        self.count = 0

    def __str__(self):
        # Return string formatted as "<name>: count=<count>"
        return f"{self.name}: count={self.count}"

    @staticmethod
    def show_total():
        # Returns the class-level total
        return Counter.total


# ==========================================
# DRIVER CODE (Matching Input/Output Example)
# ==========================================
if __name__ == "__main__":
    # 4. Create at least THREE Counter objects
    c1 = Counter("clicks")
    c2 = Counter("views")
    c3 = Counter("downloads")

    # Call increment() a different number of times on each
    for _ in range(3):
        c1.increment()

    for _ in range(5):
        c2.increment()

    c3.increment(10)

    # Reset ONE of them
    c1.reset()

    # Print each object using print(c)
    print(c1)
    print(c2)
    print(c3)

    # Print the overall Counter.total
    print(f"Total across all counters: {Counter.show_total()}")
   
