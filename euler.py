import sys
import problems
argument = sys.argv[1]
print getattr(problems, "problem%s" %argument )()
