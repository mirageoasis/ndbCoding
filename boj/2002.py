N = int(input())

in_tunnel = []
out_tunnel = []

in_tunnel_dict = dict()
out_tunnel_dict = dict()

for i in range(N):
    c = input()
    in_tunnel.append(c)
for i in range(N):
    c = input()
    out_tunnel.append(c)

in_front_list = set()

for i in in_tunnel:
    in_tunnel_dict[i] = in_front_list.copy()
    in_front_list.add(i)

out_rear_list = set()
for i in out_tunnel[-1::-1]:
    out_tunnel_dict[i] = out_rear_list.copy()
    out_rear_list.add(i)

ans = 0

for key, value in out_tunnel_dict.items():
    for out_elem in value:
        if out_elem in in_tunnel_dict[key]:
            ans+=1
            break 

print(ans)