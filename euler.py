import sys
import problems
argument = sys.argv[1]
getattr(problems, "problem%s" %argument )()



