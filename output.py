import subprocess
import telnetlib

html = """
    <table>
        <tr><th>User</th><th>Count</th><th>Color</th></tr>
        {0}
    </table>
"""

get_users = subprocess.run (["ps -Af | awk '{print $1}' | egrep -v UID | uniq -c"], stdout=subprocess.PIPE, shell=True)
s = str(get_users.stdout,'UTF-8')
s = s.split()
items = []
for i in range(0,len(s),2):
    items.append( s[i : 2 + i])   

for i in range(len(items)):
    items[i][0] = int(items[i][0])
    if items[i][0] > 10:
       items[i].append('&red')
    else:
       items[i].append('&green')    
tr = "<tr align=\"center\">{0}</tr>"
td = "<td align=\"center\">{0}</td>"
subitems = [tr.format(''.join([td.format(a) for a in item])) for item in items]
f = open('table.html','w')
f.write(html.format("".join(subitems)))
f.close 

get_users = subprocess.run (["telnet 192.168.200.3 1984 "status shift.user14 green '" + html + "'""], shell=True)

