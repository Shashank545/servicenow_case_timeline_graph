#CS0072591
#CS0045504

import pandas as pd
import graphviz
from datetime import datetime


#initialize D graph of Graphviz
d = graphviz.Digraph(filename='rank_same.gv')


#Load case time model dataframe 
case_data = pd.read_excel("case_longitudinal_view.xlsx") 
print(case_data.columns)
case_focus = case_data[case_data["CaseID"]=="CS0072591"]


case_time_list = case_focus.Timestamp.to_list()
case_event_list = case_focus.Event.to_list()
case_attr_list = case_focus["Event Attributes"].to_list()
case_attr_value_list = case_focus["Event Attribute Values"].to_list()

#For sanity checking
print(f"len of event {len(case_event_list)} - len of time {len(case_time_list)}")

#index position for time and event
total_index_list =  [0,15,17, 22, 29,34,42,55, 68, 82, 86, 117, 132, 148, 164, 180, 188]
exception = []

#Event List Creation
master_event_list = ["ITSM_CASE_CREATE",
                     "ITSM_USER_NOTIFY", 
                     "ITSM_AGENT_ASSIGN", 
                     "CDAX_CASE_DISPATCH",
                     "CDAX_CASE_CREATE",
                     "CDAX_CASE_ASSIGN",
                     "CDAX_WO_CREATE",
                     "CDAX_WO_ASSIGNMENT",
                     "CDAX_WO_CLOSING", 
                     "CDAX_WO_CANCELLATION", 
                     "CDAX_WO_RECEIVE_CONFIRMATION", 
                     "CDAX_PARTS_ORDER_CREATE", 
                     "CDAX_PARTS_ORDER_CANCELLATION",
                     "CDAX_PARTS_SHIPPING", 
                     "CDAX_PARTS_DELIVERY", 
                     "ITSM_CASE_RESOLVE", 
                     "ITSM_CASE_CLOSE"]



print(len(case_attr_list))
print(len(case_attr_value_list))

# Attribute- Value List Creation
select_attr = [case_attr_list[1],case_attr_list[2], case_attr_list[6],
                case_attr_list[16],case_attr_list[15],
                case_attr_list[17], case_attr_list[20],
                case_attr_list[26],case_attr_list[28],
                case_attr_list[29],case_attr_list[33],
                case_attr_list[34],case_attr_list[35],
                case_attr_list[44],case_attr_list[46],
                case_attr_list[57],case_attr_list[61],
                case_attr_list[71],case_attr_list[72],
                case_attr_list[84],case_attr_list[85],
                case_attr_list[88],case_attr_list[89],
                case_attr_list[119],case_attr_list[121],
                case_attr_list[133],case_attr_list[136],
                case_attr_list[150],case_attr_list[158],
                case_attr_list[167],case_attr_list[169],
                case_attr_list[180],case_attr_list[181],
                case_attr_list[188],case_attr_list[195]]


select_attr_val = [case_attr_value_list[1],case_attr_value_list[2], case_attr_value_list[6],
                    case_attr_value_list[16],case_attr_value_list[15],
                    case_attr_value_list[17], case_attr_value_list[20],
                    case_attr_value_list[26],case_attr_value_list[28],
                    case_attr_value_list[29],case_attr_value_list[33],
                    case_attr_value_list[34],case_attr_value_list[35],
                    case_attr_value_list[44],case_attr_value_list[46],
                    case_attr_value_list[57],case_attr_value_list[61],
                    case_attr_value_list[71],case_attr_value_list[72],
                    case_attr_value_list[84],case_attr_value_list[85],
                    case_attr_value_list[88],case_attr_value_list[89],
                    case_attr_value_list[119],case_attr_value_list[121],
                    case_attr_value_list[133],case_attr_value_list[136],
                    case_attr_value_list[150],case_attr_value_list[158],
                    case_attr_value_list[167],case_attr_value_list[169],
                    case_attr_value_list[180],case_attr_value_list[181],
                    case_attr_value_list[188],case_attr_value_list[195]]


str1 = [str(item[0])+" - "+str(item[1])+" \n" for item in zip(select_attr[0:3], select_attr_val[0:3])]

str2 = [str(item[0])+" - "+str(item[1])+"\n" for item in zip(select_attr[3:5], select_attr_val[3:5])]

str3 = [str(item[0])+" - "+str(item[1])+"\n" for item in zip(select_attr[5:7], select_attr_val[5:7])]

str4 = [str(item[0])+" - "+str(item[1])+"\n" for item in zip(select_attr[7:9], select_attr_val[7:9])]

str5 = [str(item[0])+" - "+str(item[1])+"\n" for item in zip(select_attr[9:11], select_attr_val[9:11])]

str6 = [str(item[0])+" - "+str(item[1])+"\n" for item in zip(select_attr[11:13], select_attr_val[11:13])]

str7 = [str(item[0])+" - "+str(item[1])+"\n" for item in zip(select_attr[13:15], select_attr_val[13:15])]

str8 = [str(item[0])+" - "+str(item[1])+"\n" for item in zip(select_attr[15:17], select_attr_val[15:17])]

str9 = [str(item[0])+" - "+str(item[1])+"\n" for item in zip(select_attr[17:19], select_attr_val[17:19])]

str10 = [str(item[0])+" - "+str(item[1])+"\n" for item in zip(select_attr[19:21], select_attr_val[19:21])]

str11 = [str(item[0])+" - "+str(item[1])+"\n" for item in zip(select_attr[21:23], select_attr_val[20:22])]

str12 = [str(item[0])+" - "+str(item[1])+"\n" for item in zip(select_attr[23:25], select_attr_val[23:25])]

str13 = [str(item[0])+" - "+str(item[1])+"\n" for item in zip(select_attr[25:27], select_attr_val[25:27])]

str14 = [str(item[0])+" - "+str(item[1])+"\n" for item in zip(select_attr[27:29], select_attr_val[27:29])]

str15 = [str(item[0])+" - "+str(item[1])+"\n" for item in zip(select_attr[29:31], select_attr_val[29:31])]

str16 = [str(item[0])+" - "+str(item[1])+"\n" for item in zip(select_attr[31:33], select_attr_val[31:33])]

str17 = [str(item[0])+" - "+str(item[1])+"\n" for item in zip(select_attr[33:36], select_attr_val[33:36])]


list_str = [str1, str2, str3, str4, str5, str6, str7, str8, str9, str10, str11, str12, str13, str14, str15, str16, str17]

print("\n")
#print(list_str)
                          
dict_display = dict(zip(master_event_list, list_str))

for k,v in dict_display.items():
    print(k ,";" ,v)

#Dynamic filtering on case specific availability
for index in total_index_list:
    if str(case_time_list[index]) =='nan':
        exception.append(index)

print(exception)

case_time_list = [case_time_list[index] for index in total_index_list if index not in exception]
case_event_list = [case_event_list[index] for index in total_index_list if index not in exception]


print(f"len of event {len(case_event_list)} - len of time {len(case_time_list)}")


#Sorting everything based on time list
zipped_lists = zip(case_time_list, case_event_list)
sorted_pairs = sorted(zipped_lists)
tuples = zip(*sorted_pairs)
case_time_list, case_event_list = [list(tuple) for tuple in tuples]

print("\n")
#print(case_event_list)


display_str_list = [dict_display[eve] for eve in case_event_list]
print("\n")

#print(display_str_list)

new_attr_list = [" ".join(x) for x in display_str_list]

#print(new_attr_list)

case_time_list = ["T"+str(i)+" = "+case_time_list[i] for i in range(len(case_time_list))]
case_attr_list = [str(k) for k in new_attr_list]

print("\n")

#print(case_attr_list)

for ev,ev1,ev2 in zip(case_event_list, case_time_list, case_attr_list):

    with d.subgraph() as s:
        s.attr(rank='same', color='lightgrey')
        s.node_attr['style'] = 'filled'
        s.node(ev)
        s.node(ev1)
        s.node(ev2)
    s.edge(ev, ev1)
    s.edge(ev1, ev2)

for i in range(len(case_event_list)-1):
    d.edge(case_event_list[i], case_event_list[i+1])

#Display The Plot
d.view()
