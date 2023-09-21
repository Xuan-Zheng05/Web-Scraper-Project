
import testingtools
import crawler
import searchdata
import search
output = open('fruits3-search-failed.txt', 'w')
success_output = open('fruits3-search-passed.txt', 'w')

#Performing crawl starting at seed http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html
crawler.crawl('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html')
#Test #0 checking search results for 'tomato papaya lime fig coconut apple kiwi' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-818.html', 'title': 'N-818', 'score': 0.9973988378173667}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-958.html', 'title': 'N-958', 'score': 0.9960536088619666}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-536.html', 'title': 'N-536', 'score': 0.9952332710620039}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-560.html', 'title': 'N-560', 'score': 0.9942600812469049}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-77.html', 'title': 'N-77', 'score': 0.9939918286932945}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-453.html', 'title': 'N-453', 'score': 0.9934438424269104}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-843.html', 'title': 'N-843', 'score': 0.9921260125571836}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-28.html', 'title': 'N-28', 'score': 0.9918922270247549}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-959.html', 'title': 'N-959', 'score': 0.9913352267255422}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-951.html', 'title': 'N-951', 'score': 0.9907036820047195}]
result = search.search('tomato papaya lime fig coconut apple kiwi',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #0 checking search results for 'tomato papaya lime fig coconut apple kiwi' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #0 checking search results for 'tomato papaya lime fig coconut apple kiwi' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #1 checking search results for 'orange papaya cherry orange pear' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-354.html', 'title': 'N-354', 'score': 0.9997022566403924}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-497.html', 'title': 'N-497', 'score': 0.9993650443476283}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-279.html', 'title': 'N-279', 'score': 0.998002867239391}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-861.html', 'title': 'N-861', 'score': 0.9971403474826719}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-558.html', 'title': 'N-558', 'score': 0.996771639857518}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-708.html', 'title': 'N-708', 'score': 0.996127011515354}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-374.html', 'title': 'N-374', 'score': 0.9958219332673957}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-131.html', 'title': 'N-131', 'score': 0.9951144851186627}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-990.html', 'title': 'N-990', 'score': 0.9950899692394906}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-849.html', 'title': 'N-849', 'score': 0.9948553607832922}]
result = search.search('orange papaya cherry orange pear',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #1 checking search results for 'orange papaya cherry orange pear' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #1 checking search results for 'orange papaya cherry orange pear' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #2 checking search results for 'papaya kiwi pear banana blueberry apple blueberry coconut' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-951.html', 'title': 'N-951', 'score': 0.993027219999454}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-592.html', 'title': 'N-592', 'score': 0.989308747131862}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-777.html', 'title': 'N-777', 'score': 0.9892226778816167}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-959.html', 'title': 'N-959', 'score': 0.9891340480845535}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-45.html', 'title': 'N-45', 'score': 0.9882368153637435}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-863.html', 'title': 'N-863', 'score': 0.9869387245290836}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-815.html', 'title': 'N-815', 'score': 0.986439215625619}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-858.html', 'title': 'N-858', 'score': 0.9852159837610533}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-820.html', 'title': 'N-820', 'score': 0.9850924395058236}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-298.html', 'title': 'N-298', 'score': 0.9843072701491941}]
result = search.search('papaya kiwi pear banana blueberry apple blueberry coconut',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #2 checking search results for 'papaya kiwi pear banana blueberry apple blueberry coconut' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #2 checking search results for 'papaya kiwi pear banana blueberry apple blueberry coconut' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #3 checking search results for 'tomato lime apricot peach orange peach' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-188.html', 'title': 'N-188', 'score': 0.9998345654100581}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-154.html', 'title': 'N-154', 'score': 0.9998049760726991}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-292.html', 'title': 'N-292', 'score': 0.99978180958317}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-839.html', 'title': 'N-839', 'score': 0.99978180958317}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-159.html', 'title': 'N-159', 'score': 0.9997752270964424}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-375.html', 'title': 'N-375', 'score': 0.9997158427337836}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-865.html', 'title': 'N-865', 'score': 0.9996533814413956}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-460.html', 'title': 'N-460', 'score': 0.9977079017731926}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-892.html', 'title': 'N-892', 'score': 0.9971782394060191}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-740.html', 'title': 'N-740', 'score': 0.9971406248827765}]
result = search.search('tomato lime apricot peach orange peach',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #3 checking search results for 'tomato lime apricot peach orange peach' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #3 checking search results for 'tomato lime apricot peach orange peach' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #4 checking search results for 'apricot papaya blueberry papaya cherry peach cherry' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-86.html', 'title': 'N-86', 'score': 0.9998970855593278}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-580.html', 'title': 'N-580', 'score': 0.9957471757630316}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-429.html', 'title': 'N-429', 'score': 0.9954424995891041}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-317.html', 'title': 'N-317', 'score': 0.9953239721608816}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-689.html', 'title': 'N-689', 'score': 0.9942103813799021}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-479.html', 'title': 'N-479', 'score': 0.9928861668270329}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-528.html', 'title': 'N-528', 'score': 0.9928555401800168}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-660.html', 'title': 'N-660', 'score': 0.9919529155717656}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-917.html', 'title': 'N-917', 'score': 0.9915437659274834}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-967.html', 'title': 'N-967', 'score': 0.9897835579090725}]
result = search.search('apricot papaya blueberry papaya cherry peach cherry',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #4 checking search results for 'apricot papaya blueberry papaya cherry peach cherry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #4 checking search results for 'apricot papaya blueberry papaya cherry peach cherry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #5 checking search results for 'orange kiwi tomato fig kiwi kiwi' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-6.html', 'title': 'N-6', 'score': 0.018491323419830803}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'title': 'N-0', 'score': 0.014495554881618692}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-10.html', 'title': 'N-10', 'score': 0.01137381300692998}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-25.html', 'title': 'N-25', 'score': 0.009768481710725547}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-4.html', 'title': 'N-4', 'score': 0.009731164047156902}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-5.html', 'title': 'N-5', 'score': 0.008731796515936505}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-2.html', 'title': 'N-2', 'score': 0.007160341848209782}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-241.html', 'title': 'N-241', 'score': 0.006342092976320602}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-7.html', 'title': 'N-7', 'score': 0.006189385721536872}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-3.html', 'title': 'N-3', 'score': 0.00599066633733096}]
result = search.search('orange kiwi tomato fig kiwi kiwi',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #5 checking search results for 'orange kiwi tomato fig kiwi kiwi' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #5 checking search results for 'orange kiwi tomato fig kiwi kiwi' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #6 checking search results for 'blueberry banana apricot apple pear kiwi' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-694.html', 'title': 'N-694', 'score': 0.9975082001944056}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-481.html', 'title': 'N-481', 'score': 0.996301213304822}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-500.html', 'title': 'N-500', 'score': 0.9956159519321971}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-351.html', 'title': 'N-351', 'score': 0.994605711014624}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-560.html', 'title': 'N-560', 'score': 0.9945196652342286}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-451.html', 'title': 'N-451', 'score': 0.9939554773764375}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-453.html', 'title': 'N-453', 'score': 0.9935436599828211}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-843.html', 'title': 'N-843', 'score': 0.9926296013992941}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-734.html', 'title': 'N-734', 'score': 0.9922953601884404}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-957.html', 'title': 'N-957', 'score': 0.991927623671633}]
result = search.search('blueberry banana apricot apple pear kiwi',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #6 checking search results for 'blueberry banana apricot apple pear kiwi' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #6 checking search results for 'blueberry banana apricot apple pear kiwi' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #7 checking search results for 'papaya blueberry peach coconut papaya apple banana peach' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-906.html', 'title': 'N-906', 'score': 0.9940295934810903}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-409.html', 'title': 'N-409', 'score': 0.9897813764602059}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-379.html', 'title': 'N-379', 'score': 0.9895159857517568}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-419.html', 'title': 'N-419', 'score': 0.9880670935721735}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-51.html', 'title': 'N-51', 'score': 0.9880290146492112}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-202.html', 'title': 'N-202', 'score': 0.9880077657632298}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-84.html', 'title': 'N-84', 'score': 0.9879211860529318}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-805.html', 'title': 'N-805', 'score': 0.9878808321065415}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-481.html', 'title': 'N-481', 'score': 0.9863620900778372}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-61.html', 'title': 'N-61', 'score': 0.9862503128968529}]
result = search.search('papaya blueberry peach coconut papaya apple banana peach',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #7 checking search results for 'papaya blueberry peach coconut papaya apple banana peach' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #7 checking search results for 'papaya blueberry peach coconut papaya apple banana peach' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #8 checking search results for 'tomato pear apple coconut banana peach pear fig' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-316.html', 'title': 'N-316', 'score': 0.9940659649063749}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-77.html', 'title': 'N-77', 'score': 0.9931128084487275}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-178.html', 'title': 'N-178', 'score': 0.9917148630901405}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-58.html', 'title': 'N-58', 'score': 0.9911684443873567}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-358.html', 'title': 'N-358', 'score': 0.990327632311481}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-56.html', 'title': 'N-56', 'score': 0.9902228412955095}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-250.html', 'title': 'N-250', 'score': 0.9901165044704642}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-102.html', 'title': 'N-102', 'score': 0.9896969432813173}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-368.html', 'title': 'N-368', 'score': 0.9877410429235957}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-20.html', 'title': 'N-20', 'score': 0.987736995399923}]
result = search.search('tomato pear apple coconut banana peach pear fig',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #8 checking search results for 'tomato pear apple coconut banana peach pear fig' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #8 checking search results for 'tomato pear apple coconut banana peach pear fig' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #9 checking search results for 'peach cherry coconut peach lime' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-292.html', 'title': 'N-292', 'score': 0.9996500748189912}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-84.html', 'title': 'N-84', 'score': 0.9996447378206377}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-736.html', 'title': 'N-736', 'score': 0.9995677145439555}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-28.html', 'title': 'N-28', 'score': 0.997276904013137}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-743.html', 'title': 'N-743', 'score': 0.9971930198766357}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-120.html', 'title': 'N-120', 'score': 0.9965308262049993}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-388.html', 'title': 'N-388', 'score': 0.9961759066313096}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-906.html', 'title': 'N-906', 'score': 0.9960500467870607}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-822.html', 'title': 'N-822', 'score': 0.9941494490710892}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-296.html', 'title': 'N-296', 'score': 0.9939396486370762}]
result = search.search('peach cherry coconut peach lime',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #9 checking search results for 'peach cherry coconut peach lime' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #9 checking search results for 'peach cherry coconut peach lime' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #10 checking search results for 'orange banana apricot peach fig' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-500.html', 'title': 'N-500', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-59.html', 'title': 'N-59', 'score': 0.9976987821548929}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-930.html', 'title': 'N-930', 'score': 0.9974270205878879}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-639.html', 'title': 'N-639', 'score': 0.9964822405654034}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-997.html', 'title': 'N-997', 'score': 0.9958771729196649}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-422.html', 'title': 'N-422', 'score': 0.9947977386996366}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-408.html', 'title': 'N-408', 'score': 0.9946661836994116}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-482.html', 'title': 'N-482', 'score': 0.994415857203448}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-351.html', 'title': 'N-351', 'score': 0.9942829158314672}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-891.html', 'title': 'N-891', 'score': 0.9942824043128611}]
result = search.search('orange banana apricot peach fig',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #10 checking search results for 'orange banana apricot peach fig' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #10 checking search results for 'orange banana apricot peach fig' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #11 checking search results for 'pear coconut apple papaya papaya lime tomato apricot' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-522.html', 'title': 'N-522', 'score': 0.9943328020563532}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-88.html', 'title': 'N-88', 'score': 0.9913853204911718}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-205.html', 'title': 'N-205', 'score': 0.9904089490890622}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-478.html', 'title': 'N-478', 'score': 0.990195132417704}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-872.html', 'title': 'N-872', 'score': 0.9897315280961835}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-809.html', 'title': 'N-809', 'score': 0.98930271334996}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-906.html', 'title': 'N-906', 'score': 0.9881198935774559}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-221.html', 'title': 'N-221', 'score': 0.9880808943909278}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-797.html', 'title': 'N-797', 'score': 0.986649734324797}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-50.html', 'title': 'N-50', 'score': 0.9855023473938855}]
result = search.search('pear coconut apple papaya papaya lime tomato apricot',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #11 checking search results for 'pear coconut apple papaya papaya lime tomato apricot' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #11 checking search results for 'pear coconut apple papaya papaya lime tomato apricot' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #12 checking search results for 'apricot coconut orange papaya pear papaya blueberry papaya' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-300.html', 'title': 'N-300', 'score': 0.9997720807083129}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-89.html', 'title': 'N-89', 'score': 0.9891164293964697}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-689.html', 'title': 'N-689', 'score': 0.9862249564958816}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-906.html', 'title': 'N-906', 'score': 0.9826586138257607}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-787.html', 'title': 'N-787', 'score': 0.9814728829866901}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-88.html', 'title': 'N-88', 'score': 0.9807894777844359}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-186.html', 'title': 'N-186', 'score': 0.9758313085104724}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-917.html', 'title': 'N-917', 'score': 0.9753067633072408}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-816.html', 'title': 'N-816', 'score': 0.9751698290309898}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-396.html', 'title': 'N-396', 'score': 0.9718430108433636}]
result = search.search('apricot coconut orange papaya pear papaya blueberry papaya',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #12 checking search results for 'apricot coconut orange papaya pear papaya blueberry papaya' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #12 checking search results for 'apricot coconut orange papaya pear papaya blueberry papaya' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #13 checking search results for 'peach blueberry lime peach pear tomato' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-385.html', 'title': 'N-385', 'score': 0.9997984576292197}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-257.html', 'title': 'N-257', 'score': 0.9997821789298288}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-837.html', 'title': 'N-837', 'score': 0.9997821789298288}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-264.html', 'title': 'N-264', 'score': 0.9997670567197625}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-359.html', 'title': 'N-359', 'score': 0.9997529950624762}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-326.html', 'title': 'N-326', 'score': 0.9997336928513822}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-375.html', 'title': 'N-375', 'score': 0.9997162919120989}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-718.html', 'title': 'N-718', 'score': 0.9995816729169487}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-294.html', 'title': 'N-294', 'score': 0.9989508837640337}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-706.html', 'title': 'N-706', 'score': 0.9981341748691731}]
result = search.search('peach blueberry lime peach pear tomato',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #13 checking search results for 'peach blueberry lime peach pear tomato' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #13 checking search results for 'peach blueberry lime peach pear tomato' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #14 checking search results for 'banana papaya peach banana apricot coconut apple apricot' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-770.html', 'title': 'N-770', 'score': 0.999843661543429}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-34.html', 'title': 'N-34', 'score': 0.993102416707543}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-231.html', 'title': 'N-231', 'score': 0.9922511154652924}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-511.html', 'title': 'N-511', 'score': 0.9913247017223219}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-325.html', 'title': 'N-325', 'score': 0.9911000961123554}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-515.html', 'title': 'N-515', 'score': 0.9903949193557886}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-310.html', 'title': 'N-310', 'score': 0.9870729001423104}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-692.html', 'title': 'N-692', 'score': 0.9870603487941858}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-538.html', 'title': 'N-538', 'score': 0.9869714319364813}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-592.html', 'title': 'N-592', 'score': 0.9858479353662355}]
result = search.search('banana papaya peach banana apricot coconut apple apricot',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #14 checking search results for 'banana papaya peach banana apricot coconut apple apricot' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #14 checking search results for 'banana papaya peach banana apricot coconut apple apricot' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #15 checking search results for 'blueberry blueberry cherry papaya coconut coconut fig apple' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-895.html', 'title': 'N-895', 'score': 0.9999492483681357}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-759.html', 'title': 'N-759', 'score': 0.9952304653974231}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-884.html', 'title': 'N-884', 'score': 0.9931239722749248}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-450.html', 'title': 'N-450', 'score': 0.9886793544937186}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-169.html', 'title': 'N-169', 'score': 0.9880612527918193}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-924.html', 'title': 'N-924', 'score': 0.9871037464096191}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-229.html', 'title': 'N-229', 'score': 0.9854622246627747}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-135.html', 'title': 'N-135', 'score': 0.9853709959893566}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-100.html', 'title': 'N-100', 'score': 0.9849720172303221}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-249.html', 'title': 'N-249', 'score': 0.9847993367458221}]
result = search.search('blueberry blueberry cherry papaya coconut coconut fig apple',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #15 checking search results for 'blueberry blueberry cherry papaya coconut coconut fig apple' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #15 checking search results for 'blueberry blueberry cherry papaya coconut coconut fig apple' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #16 checking search results for 'cherry tomato papaya cherry papaya orange peach peach' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-32.html', 'title': 'N-32', 'score': 0.9999821301241643}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-266.html', 'title': 'N-266', 'score': 0.9999731211903354}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-952.html', 'title': 'N-952', 'score': 0.9999563637146398}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-309.html', 'title': 'N-309', 'score': 0.9999522401835846}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-454.html', 'title': 'N-454', 'score': 0.9999468615345931}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-672.html', 'title': 'N-672', 'score': 0.9999371458355982}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-645.html', 'title': 'N-645', 'score': 0.9992954614181787}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-892.html', 'title': 'N-892', 'score': 0.9984947663346873}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-489.html', 'title': 'N-489', 'score': 0.9981582739463625}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-592.html', 'title': 'N-592', 'score': 0.9974144041660858}]
result = search.search('cherry tomato papaya cherry papaya orange peach peach',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #16 checking search results for 'cherry tomato papaya cherry papaya orange peach peach' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #16 checking search results for 'cherry tomato papaya cherry papaya orange peach peach' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #17 checking search results for 'apricot kiwi tomato peach peach fig cherry apricot' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-449.html', 'title': 'N-449', 'score': 0.9998562638747193}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-743.html', 'title': 'N-743', 'score': 0.9980458432581647}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-430.html', 'title': 'N-430', 'score': 0.9965565060109639}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-79.html', 'title': 'N-79', 'score': 0.9942705870466355}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-84.html', 'title': 'N-84', 'score': 0.9929655959019974}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-871.html', 'title': 'N-871', 'score': 0.9916682004951229}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-394.html', 'title': 'N-394', 'score': 0.9899600534645459}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-180.html', 'title': 'N-180', 'score': 0.9894378348515791}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-601.html', 'title': 'N-601', 'score': 0.989253343644344}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-28.html', 'title': 'N-28', 'score': 0.9892437633432594}]
result = search.search('apricot kiwi tomato peach peach fig cherry apricot',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #17 checking search results for 'apricot kiwi tomato peach peach fig cherry apricot' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #17 checking search results for 'apricot kiwi tomato peach peach fig cherry apricot' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #18 checking search results for 'cherry lime apple tomato orange fig apple' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-241.html', 'title': 'N-241', 'score': 0.9997624584910378}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-377.html', 'title': 'N-377', 'score': 0.9980467320180368}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-57.html', 'title': 'N-57', 'score': 0.9975895594280161}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-743.html', 'title': 'N-743', 'score': 0.9975588619642888}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-113.html', 'title': 'N-113', 'score': 0.9955978476731075}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-177.html', 'title': 'N-177', 'score': 0.9946331291657166}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-750.html', 'title': 'N-750', 'score': 0.993442940753454}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-191.html', 'title': 'N-191', 'score': 0.9932557157989967}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-272.html', 'title': 'N-272', 'score': 0.9931091512660477}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-900.html', 'title': 'N-900', 'score': 0.992526554781644}]
result = search.search('cherry lime apple tomato orange fig apple',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #18 checking search results for 'cherry lime apple tomato orange fig apple' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #18 checking search results for 'cherry lime apple tomato orange fig apple' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #19 checking search results for 'blueberry orange kiwi fig fig' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-751.html', 'title': 'N-751', 'score': 0.9997192419450402}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-814.html', 'title': 'N-814', 'score': 0.9996157026955198}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-711.html', 'title': 'N-711', 'score': 0.9992976769445449}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-179.html', 'title': 'N-179', 'score': 0.9984009422035064}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-615.html', 'title': 'N-615', 'score': 0.9981604143352943}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-409.html', 'title': 'N-409', 'score': 0.9980888754284309}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-821.html', 'title': 'N-821', 'score': 0.9977220437386747}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-325.html', 'title': 'N-325', 'score': 0.9971421382637823}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-97.html', 'title': 'N-97', 'score': 0.996640705830898}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-524.html', 'title': 'N-524', 'score': 0.9962946416046956}]
result = search.search('blueberry orange kiwi fig fig',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #19 checking search results for 'blueberry orange kiwi fig fig' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #19 checking search results for 'blueberry orange kiwi fig fig' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #20 checking search results for 'banana orange peach apple fig' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-768.html', 'title': 'N-768', 'score': 0.998503382640843}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-500.html', 'title': 'N-500', 'score': 0.9982523458953952}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-639.html', 'title': 'N-639', 'score': 0.9962596641430205}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-351.html', 'title': 'N-351', 'score': 0.9949787896616102}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-408.html', 'title': 'N-408', 'score': 0.994518361300216}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-893.html', 'title': 'N-893', 'score': 0.9943578663395454}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-380.html', 'title': 'N-380', 'score': 0.9936116395627611}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-267.html', 'title': 'N-267', 'score': 0.9931611149664265}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-871.html', 'title': 'N-871', 'score': 0.9926544781629352}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-102.html', 'title': 'N-102', 'score': 0.9923867710995883}]
result = search.search('banana orange peach apple fig',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #20 checking search results for 'banana orange peach apple fig' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #20 checking search results for 'banana orange peach apple fig' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #21 checking search results for 'pear apple lime apple peach tomato papaya apple' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-497.html', 'title': 'N-497', 'score': 0.9949939723518089}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-212.html', 'title': 'N-212', 'score': 0.9945745448009005}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-565.html', 'title': 'N-565', 'score': 0.9935246387218523}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-927.html', 'title': 'N-927', 'score': 0.9869581177409578}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-79.html', 'title': 'N-79', 'score': 0.9868370294129029}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-464.html', 'title': 'N-464', 'score': 0.9866105340514104}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-342.html', 'title': 'N-342', 'score': 0.9861439092922765}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-272.html', 'title': 'N-272', 'score': 0.9857757174258795}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-369.html', 'title': 'N-369', 'score': 0.9854549264481703}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-918.html', 'title': 'N-918', 'score': 0.9849396750462819}]
result = search.search('pear apple lime apple peach tomato papaya apple',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #21 checking search results for 'pear apple lime apple peach tomato papaya apple' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #21 checking search results for 'pear apple lime apple peach tomato papaya apple' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #22 checking search results for 'tomato pear blueberry pear lime kiwi banana papaya' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-439.html', 'title': 'N-439', 'score': 0.9947046714051687}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-371.html', 'title': 'N-371', 'score': 0.9915641710845258}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-323.html', 'title': 'N-323', 'score': 0.991295875928822}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-77.html', 'title': 'N-77', 'score': 0.991100446299738}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-867.html', 'title': 'N-867', 'score': 0.9905439557075385}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-482.html', 'title': 'N-482', 'score': 0.990129405945804}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-117.html', 'title': 'N-117', 'score': 0.9900532626410139}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-743.html', 'title': 'N-743', 'score': 0.9894062562949545}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-176.html', 'title': 'N-176', 'score': 0.9881239896842825}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-225.html', 'title': 'N-225', 'score': 0.9864875629412824}]
result = search.search('tomato pear blueberry pear lime kiwi banana papaya',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #22 checking search results for 'tomato pear blueberry pear lime kiwi banana papaya' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #22 checking search results for 'tomato pear blueberry pear lime kiwi banana papaya' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #23 checking search results for 'kiwi kiwi apple papaya banana apple banana fig' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-146.html', 'title': 'N-146', 'score': 0.9999306955987483}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-215.html', 'title': 'N-215', 'score': 0.9972958395374583}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-18.html', 'title': 'N-18', 'score': 0.9945294892649281}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-344.html', 'title': 'N-344', 'score': 0.9941531244566411}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-290.html', 'title': 'N-290', 'score': 0.9935225810295372}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-659.html', 'title': 'N-659', 'score': 0.9930858645238447}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-222.html', 'title': 'N-222', 'score': 0.9912675887566107}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-620.html', 'title': 'N-620', 'score': 0.9894828611021967}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-727.html', 'title': 'N-727', 'score': 0.9893647219514395}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-592.html', 'title': 'N-592', 'score': 0.9893403452124506}]
result = search.search('kiwi kiwi apple papaya banana apple banana fig',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #23 checking search results for 'kiwi kiwi apple papaya banana apple banana fig' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #23 checking search results for 'kiwi kiwi apple papaya banana apple banana fig' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #24 checking search results for 'lime apricot lime coconut papaya blueberry' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-500.html', 'title': 'N-500', 'score': 0.99894894123837}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-101.html', 'title': 'N-101', 'score': 0.9981892805896088}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-659.html', 'title': 'N-659', 'score': 0.9953222289596804}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-704.html', 'title': 'N-704', 'score': 0.9952253873712196}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-168.html', 'title': 'N-168', 'score': 0.9945314270504898}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-894.html', 'title': 'N-894', 'score': 0.9944773216717}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-979.html', 'title': 'N-979', 'score': 0.9942372270732756}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-885.html', 'title': 'N-885', 'score': 0.99413861981388}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-244.html', 'title': 'N-244', 'score': 0.9937765226917135}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-198.html', 'title': 'N-198', 'score': 0.9935128438900097}]
result = search.search('lime apricot lime coconut papaya blueberry',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #24 checking search results for 'lime apricot lime coconut papaya blueberry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #24 checking search results for 'lime apricot lime coconut papaya blueberry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #25 checking search results for 'apple papaya peach fig papaya fig fig banana' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-16.html', 'title': 'N-16', 'score': 0.9961670008514567}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-783.html', 'title': 'N-783', 'score': 0.9958864314480841}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-160.html', 'title': 'N-160', 'score': 0.993189598258255}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-405.html', 'title': 'N-405', 'score': 0.9917157140313266}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-130.html', 'title': 'N-130', 'score': 0.9882658340483473}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-374.html', 'title': 'N-374', 'score': 0.9879593679068293}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-647.html', 'title': 'N-647', 'score': 0.987817755497795}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-651.html', 'title': 'N-651', 'score': 0.9857563150590027}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-677.html', 'title': 'N-677', 'score': 0.9849100273359077}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-711.html', 'title': 'N-711', 'score': 0.9844610758046184}]
result = search.search('apple papaya peach fig papaya fig fig banana',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #25 checking search results for 'apple papaya peach fig papaya fig fig banana' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #25 checking search results for 'apple papaya peach fig papaya fig fig banana' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #26 checking search results for 'cherry kiwi blueberry fig papaya pear blueberry cherry' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-336.html', 'title': 'N-336', 'score': 0.9999795048715141}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-573.html', 'title': 'N-573', 'score': 0.9979140141727109}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-951.html', 'title': 'N-951', 'score': 0.9948001615992431}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-757.html', 'title': 'N-757', 'score': 0.992359667501505}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-820.html', 'title': 'N-820', 'score': 0.9916527215474991}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-959.html', 'title': 'N-959', 'score': 0.9902241338745082}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-759.html', 'title': 'N-759', 'score': 0.9893052457502942}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-295.html', 'title': 'N-295', 'score': 0.9884120530189017}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-924.html', 'title': 'N-924', 'score': 0.9880953283957259}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-544.html', 'title': 'N-544', 'score': 0.9878215067587992}]
result = search.search('cherry kiwi blueberry fig papaya pear blueberry cherry',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #26 checking search results for 'cherry kiwi blueberry fig papaya pear blueberry cherry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #26 checking search results for 'cherry kiwi blueberry fig papaya pear blueberry cherry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #27 checking search results for 'apple cherry kiwi kiwi banana lime' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-994.html', 'title': 'N-994', 'score': 0.9997220704325243}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-178.html', 'title': 'N-178', 'score': 0.9991397316435372}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-388.html', 'title': 'N-388', 'score': 0.9979491240630038}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-682.html', 'title': 'N-682', 'score': 0.9958338250962856}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-893.html', 'title': 'N-893', 'score': 0.9956505091773469}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-879.html', 'title': 'N-879', 'score': 0.9950342891174803}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-237.html', 'title': 'N-237', 'score': 0.9942847089910308}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-134.html', 'title': 'N-134', 'score': 0.9938354091815971}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-602.html', 'title': 'N-602', 'score': 0.9931724482678689}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-391.html', 'title': 'N-391', 'score': 0.992738996697395}]
result = search.search('apple cherry kiwi kiwi banana lime',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #27 checking search results for 'apple cherry kiwi kiwi banana lime' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #27 checking search results for 'apple cherry kiwi kiwi banana lime' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #28 checking search results for 'apricot fig cherry blueberry peach banana fig fig' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-16.html', 'title': 'N-16', 'score': 0.996959035801286}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-783.html', 'title': 'N-783', 'score': 0.9926881898574541}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-867.html', 'title': 'N-867', 'score': 0.9888265861258477}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-744.html', 'title': 'N-744', 'score': 0.9884870860799416}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-254.html', 'title': 'N-254', 'score': 0.9871914461529719}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-27.html', 'title': 'N-27', 'score': 0.9829936976564357}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-323.html', 'title': 'N-323', 'score': 0.9794569238623071}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-76.html', 'title': 'N-76', 'score': 0.9782315425748115}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-461.html', 'title': 'N-461', 'score': 0.9780512799771997}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-490.html', 'title': 'N-490', 'score': 0.977742791734848}]
result = search.search('apricot fig cherry blueberry peach banana fig fig',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #28 checking search results for 'apricot fig cherry blueberry peach banana fig fig' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #28 checking search results for 'apricot fig cherry blueberry peach banana fig fig' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #29 checking search results for 'lime kiwi lime apricot orange blueberry tomato fig' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-500.html', 'title': 'N-500', 'score': 0.9989016301805866}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-198.html', 'title': 'N-198', 'score': 0.9962400145695839}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-535.html', 'title': 'N-535', 'score': 0.9910400997852563}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-101.html', 'title': 'N-101', 'score': 0.9909607338012887}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-978.html', 'title': 'N-978', 'score': 0.9903497511407116}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-972.html', 'title': 'N-972', 'score': 0.9898810830261475}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-659.html', 'title': 'N-659', 'score': 0.9898468272507308}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-484.html', 'title': 'N-484', 'score': 0.9872040947184944}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-170.html', 'title': 'N-170', 'score': 0.9864727268574708}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-930.html', 'title': 'N-930', 'score': 0.986437287773913}]
result = search.search('lime kiwi lime apricot orange blueberry tomato fig',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #29 checking search results for 'lime kiwi lime apricot orange blueberry tomato fig' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #29 checking search results for 'lime kiwi lime apricot orange blueberry tomato fig' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #30 checking search results for 'banana lime kiwi apple cherry orange orange' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-530.html', 'title': 'N-530', 'score': 0.9999205442787766}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-323.html', 'title': 'N-323', 'score': 0.9939808945728257}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-566.html', 'title': 'N-566', 'score': 0.9921045943989544}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-574.html', 'title': 'N-574', 'score': 0.9920812103914808}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-185.html', 'title': 'N-185', 'score': 0.9902843767350803}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-487.html', 'title': 'N-487', 'score': 0.9896131103180047}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-483.html', 'title': 'N-483', 'score': 0.9882070357603097}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-765.html', 'title': 'N-765', 'score': 0.987889487563803}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-679.html', 'title': 'N-679', 'score': 0.9869642681484785}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-707.html', 'title': 'N-707', 'score': 0.9864242001045844}]
result = search.search('banana lime kiwi apple cherry orange orange',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #30 checking search results for 'banana lime kiwi apple cherry orange orange' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #30 checking search results for 'banana lime kiwi apple cherry orange orange' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #31 checking search results for 'coconut blueberry cherry lime papaya cherry' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-412.html', 'title': 'N-412', 'score': 0.9997895346819345}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-189.html', 'title': 'N-189', 'score': 0.999715299774756}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-42.html', 'title': 'N-42', 'score': 0.9956476492214632}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-594.html', 'title': 'N-594', 'score': 0.9953352857624611}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-823.html', 'title': 'N-823', 'score': 0.9930311071390412}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-463.html', 'title': 'N-463', 'score': 0.9910059842070132}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-760.html', 'title': 'N-760', 'score': 0.9907077146888558}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-49.html', 'title': 'N-49', 'score': 0.9894149582786165}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-554.html', 'title': 'N-554', 'score': 0.9889273362944756}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-850.html', 'title': 'N-850', 'score': 0.9883217227021561}]
result = search.search('coconut blueberry cherry lime papaya cherry',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #31 checking search results for 'coconut blueberry cherry lime papaya cherry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #31 checking search results for 'coconut blueberry cherry lime papaya cherry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #32 checking search results for 'kiwi cherry peach fig orange apricot' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-485.html', 'title': 'N-485', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-500.html', 'title': 'N-500', 'score': 0.998804460435563}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-59.html', 'title': 'N-59', 'score': 0.9980079145023917}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-521.html', 'title': 'N-521', 'score': 0.9969935225125715}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-882.html', 'title': 'N-882', 'score': 0.996389303751072}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-377.html', 'title': 'N-377', 'score': 0.9955474650146656}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-94.html', 'title': 'N-94', 'score': 0.9941423109474049}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-978.html', 'title': 'N-978', 'score': 0.9935238871524041}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-328.html', 'title': 'N-328', 'score': 0.9923583134630122}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-639.html', 'title': 'N-639', 'score': 0.992034577575471}]
result = search.search('kiwi cherry peach fig orange apricot',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #32 checking search results for 'kiwi cherry peach fig orange apricot' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #32 checking search results for 'kiwi cherry peach fig orange apricot' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #33 checking search results for 'apple apple lime kiwi lime apricot' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-915.html', 'title': 'N-915', 'score': 0.998591176341269}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-894.html', 'title': 'N-894', 'score': 0.9982654511930434}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-668.html', 'title': 'N-668', 'score': 0.9971702010507859}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-16.html', 'title': 'N-16', 'score': 0.9970563750440713}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-953.html', 'title': 'N-953', 'score': 0.9969017386571792}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-170.html', 'title': 'N-170', 'score': 0.9962540185339849}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-59.html', 'title': 'N-59', 'score': 0.9961223349533379}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-198.html', 'title': 'N-198', 'score': 0.9959299766183862}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-823.html', 'title': 'N-823', 'score': 0.9956964783707543}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-979.html', 'title': 'N-979', 'score': 0.9956334777257785}]
result = search.search('apple apple lime kiwi lime apricot',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #33 checking search results for 'apple apple lime kiwi lime apricot' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #33 checking search results for 'apple apple lime kiwi lime apricot' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #34 checking search results for 'peach apricot apple lime lime' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-721.html', 'title': 'N-721', 'score': 0.9997009109390499}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-513.html', 'title': 'N-513', 'score': 0.9996650926810925}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-526.html', 'title': 'N-526', 'score': 0.9996083111444712}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-128.html', 'title': 'N-128', 'score': 0.9988064696577449}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-580.html', 'title': 'N-580', 'score': 0.9986108475742942}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-519.html', 'title': 'N-519', 'score': 0.9983734528501357}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-500.html', 'title': 'N-500', 'score': 0.998130253357919}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-408.html', 'title': 'N-408', 'score': 0.9972870431847823}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-681.html', 'title': 'N-681', 'score': 0.9972121509120478}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-143.html', 'title': 'N-143', 'score': 0.9970332918955177}]
result = search.search('peach apricot apple lime lime',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #34 checking search results for 'peach apricot apple lime lime' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #34 checking search results for 'peach apricot apple lime lime' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #35 checking search results for 'lime orange pear lime orange' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-6.html', 'title': 'N-6', 'score': 0.02020515397152558}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'title': 'N-0', 'score': 0.014819784383185009}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-5.html', 'title': 'N-5', 'score': 0.011180692711910287}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-25.html', 'title': 'N-25', 'score': 0.009850028952605488}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-4.html', 'title': 'N-4', 'score': 0.009353129589165812}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-2.html', 'title': 'N-2', 'score': 0.007365505570223597}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-64.html', 'title': 'N-64', 'score': 0.006831485900422198}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-10.html', 'title': 'N-10', 'score': 0.006804285928753531}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-7.html', 'title': 'N-7', 'score': 0.006521269399038747}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-3.html', 'title': 'N-3', 'score': 0.006398706958678171}]
result = search.search('lime orange pear lime orange',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #35 checking search results for 'lime orange pear lime orange' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #35 checking search results for 'lime orange pear lime orange' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #36 checking search results for 'orange coconut lime apricot lime banana' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-676.html', 'title': 'N-676', 'score': 0.9998795838198415}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-500.html', 'title': 'N-500', 'score': 0.999833323109728}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-659.html', 'title': 'N-659', 'score': 0.9971821661478705}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-408.html', 'title': 'N-408', 'score': 0.9954840507806653}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-198.html', 'title': 'N-198', 'score': 0.9953396680384975}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-170.html', 'title': 'N-170', 'score': 0.9953196057892547}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-367.html', 'title': 'N-367', 'score': 0.9942841595474705}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-474.html', 'title': 'N-474', 'score': 0.9939781839525123}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-92.html', 'title': 'N-92', 'score': 0.9939261869258849}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-595.html', 'title': 'N-595', 'score': 0.9939166174096401}]
result = search.search('orange coconut lime apricot lime banana',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #36 checking search results for 'orange coconut lime apricot lime banana' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #36 checking search results for 'orange coconut lime apricot lime banana' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #37 checking search results for 'blueberry coconut blueberry pear apricot cherry coconut' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-59.html', 'title': 'N-59', 'score': 0.9954028752352615}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-364.html', 'title': 'N-364', 'score': 0.9933919303237376}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-983.html', 'title': 'N-983', 'score': 0.9933587909802201}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-152.html', 'title': 'N-152', 'score': 0.9932093265429333}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-884.html', 'title': 'N-884', 'score': 0.9927652692317485}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-460.html', 'title': 'N-460', 'score': 0.9926529605689697}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-759.html', 'title': 'N-759', 'score': 0.9922299308807933}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-299.html', 'title': 'N-299', 'score': 0.9909657106025151}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-583.html', 'title': 'N-583', 'score': 0.9903504120533609}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-212.html', 'title': 'N-212', 'score': 0.9899615733871594}]
result = search.search('blueberry coconut blueberry pear apricot cherry coconut',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #37 checking search results for 'blueberry coconut blueberry pear apricot cherry coconut' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #37 checking search results for 'blueberry coconut blueberry pear apricot cherry coconut' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #38 checking search results for 'kiwi cherry pear peach tomato' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-996.html', 'title': 'N-996', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-59.html', 'title': 'N-59', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-598.html', 'title': 'N-598', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-646.html', 'title': 'N-646', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-886.html', 'title': 'N-886', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-166.html', 'title': 'N-166', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-560.html', 'title': 'N-560', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-584.html', 'title': 'N-584', 'score': 0.9984305788259111}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-500.html', 'title': 'N-500', 'score': 0.998409411956437}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-882.html', 'title': 'N-882', 'score': 0.9979451812036009}]
result = search.search('kiwi cherry pear peach tomato',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #38 checking search results for 'kiwi cherry pear peach tomato' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #38 checking search results for 'kiwi cherry pear peach tomato' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #39 checking search results for 'peach blueberry peach coconut kiwi blueberry cherry kiwi' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-912.html', 'title': 'N-912', 'score': 0.9947774930574396}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-388.html', 'title': 'N-388', 'score': 0.9942031877529462}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-761.html', 'title': 'N-761', 'score': 0.9937100685218464}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-51.html', 'title': 'N-51', 'score': 0.9935745783299863}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-762.html', 'title': 'N-762', 'score': 0.9927445142426533}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-902.html', 'title': 'N-902', 'score': 0.991284260762666}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-130.html', 'title': 'N-130', 'score': 0.9910467573949496}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-662.html', 'title': 'N-662', 'score': 0.9900994014346398}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-172.html', 'title': 'N-172', 'score': 0.9895253794322091}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-727.html', 'title': 'N-727', 'score': 0.9884490074883415}]
result = search.search('peach blueberry peach coconut kiwi blueberry cherry kiwi',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #39 checking search results for 'peach blueberry peach coconut kiwi blueberry cherry kiwi' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #39 checking search results for 'peach blueberry peach coconut kiwi blueberry cherry kiwi' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #40 checking search results for 'fig peach banana cherry peach peach' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-386.html', 'title': 'N-386', 'score': 0.9999938077185067}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-278.html', 'title': 'N-278', 'score': 0.9993108320975316}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-984.html', 'title': 'N-984', 'score': 0.9990706972433592}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-241.html', 'title': 'N-241', 'score': 0.9990235519372771}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-914.html', 'title': 'N-914', 'score': 0.9970760738974241}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-847.html', 'title': 'N-847', 'score': 0.995922553213618}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-202.html', 'title': 'N-202', 'score': 0.9953333242743563}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-481.html', 'title': 'N-481', 'score': 0.9949413506526479}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-124.html', 'title': 'N-124', 'score': 0.992050844991988}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-976.html', 'title': 'N-976', 'score': 0.9910971202573865}]
result = search.search('fig peach banana cherry peach peach',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #40 checking search results for 'fig peach banana cherry peach peach' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #40 checking search results for 'fig peach banana cherry peach peach' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #41 checking search results for 'orange peach peach kiwi peach kiwi pear apple' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-887.html', 'title': 'N-887', 'score': 0.9945412754069187}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-602.html', 'title': 'N-602', 'score': 0.9924981214635334}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-502.html', 'title': 'N-502', 'score': 0.9886182388524327}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-122.html', 'title': 'N-122', 'score': 0.9863301426565866}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-795.html', 'title': 'N-795', 'score': 0.986177452509339}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-755.html', 'title': 'N-755', 'score': 0.9858247016288211}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-379.html', 'title': 'N-379', 'score': 0.9857527144119513}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-32.html', 'title': 'N-32', 'score': 0.9855736925929874}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-803.html', 'title': 'N-803', 'score': 0.9851761955313761}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-426.html', 'title': 'N-426', 'score': 0.9844650500316806}]
result = search.search('orange peach peach kiwi peach kiwi pear apple',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #41 checking search results for 'orange peach peach kiwi peach kiwi pear apple' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #41 checking search results for 'orange peach peach kiwi peach kiwi pear apple' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #42 checking search results for 'kiwi coconut fig peach blueberry orange apricot' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-713.html', 'title': 'N-713', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-500.html', 'title': 'N-500', 'score': 0.9982479244757235}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-178.html', 'title': 'N-178', 'score': 0.9949565730430712}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-94.html', 'title': 'N-94', 'score': 0.9932059139794429}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-571.html', 'title': 'N-571', 'score': 0.9918484908785781}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-482.html', 'title': 'N-482', 'score': 0.9908191124148066}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-521.html', 'title': 'N-521', 'score': 0.9895975090083686}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-351.html', 'title': 'N-351', 'score': 0.9894905302208092}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-787.html', 'title': 'N-787', 'score': 0.9894548866856673}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-126.html', 'title': 'N-126', 'score': 0.9892153932550487}]
result = search.search('kiwi coconut fig peach blueberry orange apricot',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #42 checking search results for 'kiwi coconut fig peach blueberry orange apricot' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #42 checking search results for 'kiwi coconut fig peach blueberry orange apricot' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #43 checking search results for 'pear papaya tomato lime pear cherry' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-811.html', 'title': 'N-811', 'score': 0.999872196953201}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-196.html', 'title': 'N-196', 'score': 0.9998549493377685}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-669.html', 'title': 'N-669', 'score': 0.9998069064143971}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-652.html', 'title': 'N-652', 'score': 0.9998069064143971}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-825.html', 'title': 'N-825', 'score': 0.9976070310746178}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-867.html', 'title': 'N-867', 'score': 0.99753919917191}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-650.html', 'title': 'N-650', 'score': 0.9975391945472866}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-720.html', 'title': 'N-720', 'score': 0.9963076267816068}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-275.html', 'title': 'N-275', 'score': 0.9956669015094348}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-162.html', 'title': 'N-162', 'score': 0.9952687444882411}]
result = search.search('pear papaya tomato lime pear cherry',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #43 checking search results for 'pear papaya tomato lime pear cherry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #43 checking search results for 'pear papaya tomato lime pear cherry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #44 checking search results for 'blueberry apricot apricot orange fig apricot orange' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-125.html', 'title': 'N-125', 'score': 0.9994425239517255}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-261.html', 'title': 'N-261', 'score': 0.9944631230032764}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-307.html', 'title': 'N-307', 'score': 0.9943159813202103}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-801.html', 'title': 'N-801', 'score': 0.9925610396218107}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-384.html', 'title': 'N-384', 'score': 0.9918570822531622}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-645.html', 'title': 'N-645', 'score': 0.9916274130933216}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-420.html', 'title': 'N-420', 'score': 0.9905214755384774}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-18.html', 'title': 'N-18', 'score': 0.9900929042445056}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-414.html', 'title': 'N-414', 'score': 0.9895365574323154}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-503.html', 'title': 'N-503', 'score': 0.9888278424434342}]
result = search.search('blueberry apricot apricot orange fig apricot orange',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #44 checking search results for 'blueberry apricot apricot orange fig apricot orange' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #44 checking search results for 'blueberry apricot apricot orange fig apricot orange' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #45 checking search results for 'peach coconut blueberry blueberry pear coconut papaya peach' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-382.html', 'title': 'N-382', 'score': 0.9999083576488914}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-232.html', 'title': 'N-232', 'score': 0.9971865478003834}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-752.html', 'title': 'N-752', 'score': 0.994956598130286}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-521.html', 'title': 'N-521', 'score': 0.9945078395529334}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-249.html', 'title': 'N-249', 'score': 0.9934896690519193}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-372.html', 'title': 'N-372', 'score': 0.9932979661426663}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-473.html', 'title': 'N-473', 'score': 0.9927594347616415}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-885.html', 'title': 'N-885', 'score': 0.9917871631249282}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-305.html', 'title': 'N-305', 'score': 0.9917814368214908}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-66.html', 'title': 'N-66', 'score': 0.9911875226355843}]
result = search.search('peach coconut blueberry blueberry pear coconut papaya peach',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #45 checking search results for 'peach coconut blueberry blueberry pear coconut papaya peach' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #45 checking search results for 'peach coconut blueberry blueberry pear coconut papaya peach' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #46 checking search results for 'lime blueberry peach blueberry cherry cherry' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-748.html', 'title': 'N-748', 'score': 0.9998728315686272}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-853.html', 'title': 'N-853', 'score': 0.9996905832322541}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-968.html', 'title': 'N-968', 'score': 0.9983235336238206}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-80.html', 'title': 'N-80', 'score': 0.9972438248783546}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-491.html', 'title': 'N-491', 'score': 0.9969727371588897}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-195.html', 'title': 'N-195', 'score': 0.9963994073756419}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-50.html', 'title': 'N-50', 'score': 0.9963666947245878}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-558.html', 'title': 'N-558', 'score': 0.9957680401155301}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-5.html', 'title': 'N-5', 'score': 0.9954681256478377}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-297.html', 'title': 'N-297', 'score': 0.9953303339916488}]
result = search.search('lime blueberry peach blueberry cherry cherry',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #46 checking search results for 'lime blueberry peach blueberry cherry cherry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #46 checking search results for 'lime blueberry peach blueberry cherry cherry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #47 checking search results for 'fig fig fig coconut papaya papaya orange' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-451.html', 'title': 'N-451', 'score': 0.9980283563450447}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-130.html', 'title': 'N-130', 'score': 0.9967515373247159}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-163.html', 'title': 'N-163', 'score': 0.9966508055544842}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-869.html', 'title': 'N-869', 'score': 0.9936921329328823}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-619.html', 'title': 'N-619', 'score': 0.9932604704987382}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-325.html', 'title': 'N-325', 'score': 0.9908975220229832}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-468.html', 'title': 'N-468', 'score': 0.9905864905230275}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-148.html', 'title': 'N-148', 'score': 0.9905624701371456}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-979.html', 'title': 'N-979', 'score': 0.9903981694973183}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-462.html', 'title': 'N-462', 'score': 0.9901576829553658}]
result = search.search('fig fig fig coconut papaya papaya orange',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #47 checking search results for 'fig fig fig coconut papaya papaya orange' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #47 checking search results for 'fig fig fig coconut papaya papaya orange' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #48 checking search results for 'fig orange cherry fig pear banana lime peach' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-280.html', 'title': 'N-280', 'score': 0.9939238184560498}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-677.html', 'title': 'N-677', 'score': 0.9921793593859809}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-364.html', 'title': 'N-364', 'score': 0.9894151108523654}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-131.html', 'title': 'N-131', 'score': 0.9880287911258097}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-746.html', 'title': 'N-746', 'score': 0.9875557297678281}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-565.html', 'title': 'N-565', 'score': 0.9873128901725442}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-711.html', 'title': 'N-711', 'score': 0.9864059841817222}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-858.html', 'title': 'N-858', 'score': 0.9863796718293443}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-67.html', 'title': 'N-67', 'score': 0.984330328455741}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-777.html', 'title': 'N-777', 'score': 0.9843278492341485}]
result = search.search('fig orange cherry fig pear banana lime peach',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #48 checking search results for 'fig orange cherry fig pear banana lime peach' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #48 checking search results for 'fig orange cherry fig pear banana lime peach' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #49 checking search results for 'fig fig apricot banana coconut cherry kiwi' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-179.html', 'title': 'N-179', 'score': 0.9942132985946753}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-744.html', 'title': 'N-744', 'score': 0.993772003131302}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-708.html', 'title': 'N-708', 'score': 0.9928163946590173}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-143.html', 'title': 'N-143', 'score': 0.992506694829754}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-867.html', 'title': 'N-867', 'score': 0.9915138011883543}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-565.html', 'title': 'N-565', 'score': 0.991440776703649}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-858.html', 'title': 'N-858', 'score': 0.990375962463003}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-312.html', 'title': 'N-312', 'score': 0.988729538664156}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-938.html', 'title': 'N-938', 'score': 0.9886762719402664}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-595.html', 'title': 'N-595', 'score': 0.9876078358586511}]
result = search.search('fig fig apricot banana coconut cherry kiwi',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #49 checking search results for 'fig fig apricot banana coconut cherry kiwi' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #49 checking search results for 'fig fig apricot banana coconut cherry kiwi' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #50 checking search results for 'coconut orange blueberry blueberry blueberry' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-398.html', 'title': 'N-398', 'score': 0.9999999906150442}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-949.html', 'title': 'N-949', 'score': 0.9999746883285726}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-462.html', 'title': 'N-462', 'score': 0.9997465852679686}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-722.html', 'title': 'N-722', 'score': 0.9996798345483477}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-582.html', 'title': 'N-582', 'score': 0.9995954745194412}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-559.html', 'title': 'N-559', 'score': 0.9995490921829611}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-848.html', 'title': 'N-848', 'score': 0.9993344315298404}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-192.html', 'title': 'N-192', 'score': 0.9989462424232859}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-945.html', 'title': 'N-945', 'score': 0.998916971698805}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-729.html', 'title': 'N-729', 'score': 0.9988516075902264}]
result = search.search('coconut orange blueberry blueberry blueberry',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #50 checking search results for 'coconut orange blueberry blueberry blueberry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #50 checking search results for 'coconut orange blueberry blueberry blueberry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #51 checking search results for 'pear orange lime kiwi apple cherry' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-793.html', 'title': 'N-793', 'score': 0.9999999999999999}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-193.html', 'title': 'N-193', 'score': 0.998817652871167}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-333.html', 'title': 'N-333', 'score': 0.9968495272654115}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-541.html', 'title': 'N-541', 'score': 0.9951956515822197}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-28.html', 'title': 'N-28', 'score': 0.992871583162411}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-886.html', 'title': 'N-886', 'score': 0.992594734345563}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-734.html', 'title': 'N-734', 'score': 0.9916360428661365}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-687.html', 'title': 'N-687', 'score': 0.991472859083307}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-711.html', 'title': 'N-711', 'score': 0.9912836793629517}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-958.html', 'title': 'N-958', 'score': 0.9902027507906157}]
result = search.search('pear orange lime kiwi apple cherry',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #51 checking search results for 'pear orange lime kiwi apple cherry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #51 checking search results for 'pear orange lime kiwi apple cherry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


output.close()
success_output.close()
