# import  plot_benchmark.plot_method as ben
import  plot_benchmark.plot_adwin as ben

# w_list = [1,3,5]
# i_list = [100,500,1000]
w_list = [1]
i_list = [100]
result = []
for i in w_list:
    for j in i_list:
        a = ben.plotbench(_len=j,_width=i,cheb_windows_size=1000)
        # a = ben.plotADWIN(_len=j,_width=i)
        result.append(a)
        ben.plot_result(a)
# b = ben.plot_result(result)