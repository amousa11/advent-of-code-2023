import functools
index = { 'x': 0, 'm': 1, 'a': 2, 's': 3 }

# Part 1
def evaluateRule(rule, part):
    if ':' in rule:
      [condition, dest] = rule.split(":")
      [component, operator, value] = condition[0], condition[1], condition[2:]
      value = int(value)
      if operator == '<' and part[index[component]] < value:
          return dest
      elif operator == '>' and part[index[component]] > value:
          return dest
      else:
          return None
    else:
      return rule

def getAcceptedParts(input):
   [workflows, parts] = input.split("\n\n")
   workflows = workflows.splitlines()
   parts = parts.splitlines()

   flow = {}

   for workflow in workflows:
       [name, rules] = workflow.split('{')
       flow[name] = []
       rules = rules[:-1].split(',')
       flow[name] = rules

   ans = 0
   for part in parts:
        part = part[1:-1].split(',')
        part = tuple(map(lambda x: int(x[2:]), part))

        cur = 'in'
        while cur != 'A' and cur != 'R':
            rules = flow[cur]
            for rule in rules:
                cur = evaluateRule(rule, part)
                if cur != None:
                   break
        if cur == 'A':
            ans += sum(part)
   return ans 
                

test = """px{a<2006:qkq,m>2090:A,rfg}
pv{a>1716:R,A}
lnx{m>1548:A,A}
rfg{s<537:gd,x>2440:R,A}
qs{s>3448:A,lnx}
qkq{x<1416:A,crn}
crn{x>2662:A,R}
in{s<1351:px,qqz}
qqz{s>2770:qs,m<1801:hdj,R}
gd{a>3333:R,R}
hdj{m>838:A,pv}

{x=787,m=2655,a=1222,s=2876}
{x=1679,m=44,a=2067,s=496}
{x=2036,m=264,a=79,s=2244}
{x=2461,m=1339,a=466,s=291}
{x=2127,m=1623,a=2188,s=1013}"""

print(getAcceptedParts(test))
print(getAcceptedParts(open("inputs/day19.txt", "r").read()))

# Part 2

def splitRanges(ranges, component, value, lt):
    i = index[component]
    rangeI = ranges[i]
    if not (ranges[i][0] <= value <= ranges[i][1]):
        return []

    lValue = value - 1 if lt else value
    rValue = value if lt else value + 1
    
    return [(*ranges[:i], (rangeI[0], lValue), *ranges[i+1:]), (*ranges[:i], (rValue, rangeI[1]), *ranges[i+1:])]

def getNumAccepted(input):
   [workflows, parts] = input.split("\n\n")
   workflows = workflows.splitlines()
   parts = parts.splitlines()

   flow = {}

   for workflow in workflows:
       [name, rules] = workflow.split('{')
       flow[name] = []
       rules = rules[:-1].split(',')
       flow[name] = rules

   ans = []
   stack = [('in', 0, ((1, 4000),(1, 4000), (1, 4000), (1, 4000)))]
   while stack:
       cur, ruleIndex, ranges = stack.pop()
       if cur == 'A':
           ans.append(ranges)
           continue
       elif cur == 'R':
           continue

       rule = flow[cur][ruleIndex] 
       if ':' in rule:
         [condition, dest] = rule.split(":")
         [component, operator, value] = condition[0], condition[1], condition[2:]
         value = int(value)
         if operator == '<':
            [lRanges, rRanges] = splitRanges(ranges, component, value, True)
            stack.append((dest, 0, lRanges))
            stack.append((cur, ruleIndex+1, rRanges))
         elif operator == '>':
            [lRanges, rRanges] = splitRanges(ranges, component, value, False) 
            stack.append((dest, 0, rRanges))
            stack.append((cur, ruleIndex+1, lRanges))
       else:
            stack.append((rule, 0, ranges))
   combinations = 0
   for ranges in ans:
       combinations += functools.reduce(lambda x,y: x * y, map(lambda x: 1 + x[1] - x[0], ranges))
   return combinations 

print(getNumAccepted(test))
print(getNumAccepted(open("inputs/day19.txt", "r").read()))
