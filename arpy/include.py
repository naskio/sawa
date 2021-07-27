# # print
#
# def اطبع(*args, sep='', end='\n', file=None):
#     num_dict = {"0": "٠", "1": "١", "2": "٢", "3": "٣", "4": "٤", "5": "٥", "6": "٦", "7": "٧", "8": "٨", "9": "٩"}
#     res = ""
#     for arg in args:
#         args = str(arg)
#         for num in num_dict.keys():
#             if num in arg:
#                 arg = args.replace(num, num_dict[num])
#         res += arg + sep
#     print(res, sep=sep, end=end, file=file)
#
# # print
