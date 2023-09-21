
import testingtools
import crawler
import searchdata
import search
output = open('fruits5-page-rank-failed.txt', 'w')
success_output = open('fruits5-page-rank-passed.txt', 'w')

#Performing crawl starting at seed http://people.scs.carleton.ca/~davidmckenney/fruits5/N-0.html
crawler.crawl('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-0.html')
#Test #0 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-67.html
expected = 0.0007559546643606753
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-67.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #0 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-67.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #0 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-67.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #1 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-63.html
expected = 0.007079246730102673
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-63.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #1 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-63.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #1 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-63.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #2 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-59.html
expected = 0.002366560682972148
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-59.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #2 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-59.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #2 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-59.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #3 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-722.html
expected = 0.00038827248057796143
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-722.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #3 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-722.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #3 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-722.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #4 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-995.html
expected = 0.0003746979982437305
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-995.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #4 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-995.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #4 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-995.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #5 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-796.html
expected = 0.00040117909978909706
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-796.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #5 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-796.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #5 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-796.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #6 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-877.html
expected = 0.0006744066352629891
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-877.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #6 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-877.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #6 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-877.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #7 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-807.html
expected = 0.000360004864997057
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-807.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #7 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-807.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #7 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-807.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #8 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-986.html
expected = 0.0006903066698715218
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-986.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #8 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-986.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #8 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-986.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #9 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-159.html
expected = 0.0012759484109147686
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-159.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #9 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-159.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #9 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-159.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #10 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-645.html
expected = 0.001484623711668002
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-645.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #10 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-645.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #10 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-645.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #11 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-490.html
expected = 0.0012810357978514807
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-490.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #11 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-490.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #11 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-490.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #12 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-530.html
expected = 0.00035474686013413495
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-530.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #12 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-530.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #12 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-530.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #13 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-726.html
expected = 0.00038854549750193625
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-726.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #13 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-726.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #13 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-726.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #14 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-639.html
expected = 0.00035714372225053464
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-639.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #14 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-639.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #14 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-639.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #15 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-562.html
expected = 0.001296140235741426
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-562.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #15 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-562.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #15 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-562.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #16 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-61.html
expected = 0.00035816970936534325
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-61.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #16 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-61.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #16 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-61.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #17 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-314.html
expected = 0.0012925521566352518
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-314.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #17 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-314.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #17 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-314.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #18 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-561.html
expected = 0.0006381885194083441
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-561.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #18 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-561.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #18 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-561.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #19 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-517.html
expected = 0.0006159942140834029
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-517.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #19 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-517.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #19 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-517.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #20 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-614.html
expected = 0.0011706148736942389
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-614.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #20 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-614.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #20 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-614.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #21 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-634.html
expected = 0.0003985108295820871
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-634.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #21 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-634.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #21 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-634.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #22 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-838.html
expected = 0.0004011813250807284
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-838.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #22 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-838.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #22 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-838.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #23 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-79.html
expected = 0.002145161240578274
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-79.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #23 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-79.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #23 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-79.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #24 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-725.html
expected = 0.0003594694366714369
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-725.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #24 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-725.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #24 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-725.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #25 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-674.html
expected = 0.0006579592746291063
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-674.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #25 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-674.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #25 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-674.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #26 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-861.html
expected = 0.0003878230988160015
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-861.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #26 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-861.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #26 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-861.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #27 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-362.html
expected = 0.0007984881367083571
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-362.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #27 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-362.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #27 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-362.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #28 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-153.html
expected = 0.0023263904203868853
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-153.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #28 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-153.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #28 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-153.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #29 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-533.html
expected = 0.0004150691705514561
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-533.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #29 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-533.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #29 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-533.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #30 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-282.html
expected = 0.002654562185314341
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-282.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #30 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-282.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #30 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-282.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #31 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-179.html
expected = 0.0012022548681517196
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-179.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #31 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-179.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #31 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-179.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #32 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-190.html
expected = 0.0013780229780845563
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-190.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #32 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-190.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #32 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-190.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #33 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-920.html
expected = 0.0006743627530856482
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-920.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #33 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-920.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #33 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-920.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #34 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-336.html
expected = 0.0006347946140478097
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-336.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #34 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-336.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #34 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-336.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #35 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-288.html
expected = 0.0005108494730696944
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-288.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #35 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-288.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #35 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-288.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #36 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-60.html
expected = 0.005182060518420735
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-60.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #36 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-60.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #36 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-60.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #37 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-439.html
expected = 0.0003510555162011743
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-439.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #37 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-439.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #37 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-439.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #38 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-598.html
expected = 0.0006369960263928504
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-598.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #38 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-598.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #38 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-598.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #39 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-254.html
expected = 0.002823100241940467
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-254.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #39 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-254.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #39 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-254.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #40 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-353.html
expected = 0.0003645893943690289
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-353.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #40 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-353.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #40 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-353.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #41 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-334.html
expected = 0.0008917921783882647
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-334.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #41 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-334.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #41 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-334.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #42 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-673.html
expected = 0.0008761886931068969
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-673.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #42 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-673.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #42 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-673.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #43 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-932.html
expected = 0.0006483693820357861
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-932.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #43 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-932.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #43 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-932.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #44 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-687.html
expected = 0.0004105168625576258
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-687.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #44 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-687.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #44 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-687.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #45 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-340.html
expected = 0.0010756602570563586
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-340.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #45 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-340.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #45 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-340.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #46 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-563.html
expected = 0.000994319886062199
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-563.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #46 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-563.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #46 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-563.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #47 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-745.html
expected = 0.00035925602547880794
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-745.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #47 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-745.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #47 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-745.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #48 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-934.html
expected = 0.00039825673559476803
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-934.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #48 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-934.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #48 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-934.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #49 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-322.html
expected = 0.00036180612842542134
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-322.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #49 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-322.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #49 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-322.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #50 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html
expected = -1
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #50 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #50 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


output.close()
success_output.close()
