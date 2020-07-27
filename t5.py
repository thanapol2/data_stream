import  plot_benchmark.plot_method as ben

w_list = [1,3,5]
i_list = [100,500,1000]
# w_list = [1]
# i_list = [100]
result = []
for i in w_list:
    for j in i_list:
        a = ben.plotbench(_len=j,_width=i,cheb_windows_size=1000)
        result.append(a)