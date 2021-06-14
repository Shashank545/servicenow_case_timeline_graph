import numpy as np
import pandas as pd


#Importing Servicenow datafiles
#case
case_df = pd.read_csv("sn_customerservice_case_April29_2021.csv", encoding = 'latin1')
#task
task_df = pd.read_csv("sn_customerservice_task_April29_2021.csv", encoding = 'latin1')
#part
part_df = pd.read_csv("u_parts_order_April29_2021.csv", encoding = 'latin1')
#asset
asset_df = pd.read_csv("CDHS_alm_asset.csv", encoding = 'latin1')



output_columns_df = pd.read_excel("ITSM Lifecycle Modeling_v11.xlsx", sheet_name=2)
output_columns = output_columns_df["Actual variables pool"].dropna().to_list()

time_columns = ["opened_at", #case
                "sys_created_on", #case
                "assigned_on", #case
                "u_case_dispatched_to_cdax", #case
                "u_case_created_in_cdax", #case
                "u_case_assigned_in_cdax", #case
                "opened_at", #task
                "u_early_start_date", #task
                "closed_at", #task
                "sys_updated_on", #task
                "u_latest_start_date", #task
                "cdax_booking_create_timestamp", #book
                "cdax_booking_scheduled_timestamp", #book
                "cdax_booking_complete_timestamp", #book
                "opened_at", #part
                "sys_updated_on", #part
                "u_ship_date", #part
                "u_expected_delivery_date", #part
                "resolved_at", #case
                "closed_at"] #case




# create an Empty DataFrame object With column names only
df = pd.DataFrame(columns = output_columns)
print(df)

template_dflist = []
cases = ['CS0072591','CS0059768','CS0081372','CS0065260','CS0062221','CS0057060','CS0010703','CS0067938','CS0013071','CS0043603']

case_list = case_df.number.to_list()
print(len(case_list))
parts_case_list = part_df.parent.to_list()
print(len(parts_case_list))
tasks_case_list = task_df.parent.to_list()
print(len(tasks_case_list))

common_cases = list(set(case_list).intersection(set(parts_case_list)).intersection(set(tasks_case_list)))
print(len(common_cases))



#Event Management

event_list = ["ITSM_CASE_CREATE",
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
            "CDAX_BOOKING_CREATION",
            "CDAX_BOOKING_SCHEDULE", 
            "CDAX_BOOKING_COMPLETED", 
            "CDAX_PARTS_ORDER_CREATE", 
            "CDAX_PARTS_ORDER_CANCELLATION",
            "CDAX_PARTS_SHIPPING", 
            "CDAX_PARTS_DELIVERY", 
            "ITSM_CASE_RESOLVE", 
            "ITSM_CASE_CLOSE"]

event_index_list =  [0,15,17, 22, 29,34,42,55, 68, 82, 86, 90, 99, 108, 117, 132, 148, 164, 180, 188]

event_dict = dict(zip(event_index_list, event_list))
event = []

print(event_dict[0])

for i in range(len(output_columns)):
    print(i)
    if i in event_index_list:
        event.insert(i,event_dict[i])
    else:
        event.insert(i,None)


# append rows to an empty DataFrame
for case in common_cases:
    row_value = []
  

    times_list = [
                case_df[case_df.number==case][time_columns[0]].iloc[0],
                case_df[case_df.number==case][time_columns[1]].iloc[0],
                case_df[case_df.number==case][time_columns[2]].iloc[0],
                case_df[case_df.number==case][time_columns[3]].iloc[0],
                case_df[case_df.number==case][time_columns[4]].iloc[0],
                case_df[case_df.number==case][time_columns[5]].iloc[0],
                task_df[task_df.parent==case][time_columns[6]].iloc[0],
                task_df[task_df.parent==case][time_columns[7]].iloc[0],
                task_df[task_df.parent==case][time_columns[8]].iloc[0],
                task_df[task_df.parent==case][time_columns[9]].iloc[0],
                task_df[task_df.parent==case][time_columns[10]].iloc[0],
                "Not Available", #book_df[book_df.number==case][time_columns[11]].iloc[0],
                "Not Available", #book_df[book_df.number==case][time_columns[12]].iloc[0],
                "Not Available", #book_df[book_df.number==case][time_columns[13]].iloc[0],
                part_df[part_df.parent==case][time_columns[14]].iloc[0],
                part_df[part_df.parent==case][time_columns[15]].iloc[0],
                part_df[part_df.parent==case][time_columns[16]].iloc[0],
                part_df[part_df.parent==case][time_columns[17]].iloc[0],
                case_df[case_df.number==case][time_columns[18]].iloc[0],
                case_df[case_df.number==case][time_columns[19]].iloc[0]
                ]
    time_index_list =  [0,15,17, 22, 29,34,42,55, 68, 82, 86, 90, 99, 108, 117, 132, 148, 164, 180, 188]
    time_dict = dict(zip(time_index_list, times_list))
    time = []
    print(time_dict[0])
    for i in range(len(output_columns)):
        print(i)
        if i in time_index_list:
            time.insert(i,time_dict[i])
        else:
            time.insert(i,None)

    case_column = [case]*len(output_columns)

    
    for i, col in enumerate(output_columns):
        
        #print(i,col,case)
        
        if col in case_df.columns:
            row_value.append(case_df[case_df.number==case][col].iloc[0])
        elif col in task_df.columns:
            row_value.append(task_df[task_df.parent==case][col].iloc[0])
        elif col in part_df.columns:
            row_value.append(part_df[part_df.parent==case][col].iloc[0])
        else:
            row_value.append("Not Available")
    print(len(row_value))

            
    #df = df.append(row_dict, ignore_index = True)
    #template_dflist.append(pd.DataFrame(row_value, index=output_columns, columns=["Case"]))
    template_dflist.append(pd.DataFrame({"CaseID":case_column, "Timestamp":time, "Event":event, "Event Attributes":output_columns, "Event Attribute Values":row_value}))
    
    
outdf = pd.concat(template_dflist, axis=0)
print(outdf.columns)

writer = pd.ExcelWriter('output.xlsx')
outdf.to_excel(writer)
# save the excel
writer.save()
print('DataFrame is written successfully to Excel File.')



