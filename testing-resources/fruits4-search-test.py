
import testingtools
import crawler
import searchdata
import search
output = open('fruits4-search-failed.txt', 'w')
success_output = open('fruits4-search-passed.txt', 'w')

#Performing crawl starting at seed http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html
crawler.crawl('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html')
#Test #0 checking search results for 'cherry blueberry orange peach apricot apple' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-383.html', 'title': 'N-383', 'score': 0.9979483354766432}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-41.html', 'title': 'N-41', 'score': 0.9970169930034828}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-824.html', 'title': 'N-824', 'score': 0.9967712107717592}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-231.html', 'title': 'N-231', 'score': 0.9962795640606839}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-662.html', 'title': 'N-662', 'score': 0.995820507041874}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-967.html', 'title': 'N-967', 'score': 0.9954069224833527}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-83.html', 'title': 'N-83', 'score': 0.9952302214669959}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-497.html', 'title': 'N-497', 'score': 0.9942304203931474}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-752.html', 'title': 'N-752', 'score': 0.9937296004247234}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-647.html', 'title': 'N-647', 'score': 0.9932001535041952}]
result = search.search('cherry blueberry orange peach apricot apple',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #0 checking search results for 'cherry blueberry orange peach apricot apple' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #0 checking search results for 'cherry blueberry orange peach apricot apple' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #1 checking search results for 'peach banana orange orange cherry cherry' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-12.html', 'title': 'N-12', 'score': 0.016305578872621598}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html', 'title': 'N-3', 'score': 0.015261520825966834}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html', 'title': 'N-1', 'score': 0.013582784559086446}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html', 'title': 'N-0', 'score': 0.013075992350951037}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-15.html', 'title': 'N-15', 'score': 0.007923050992166674}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-4.html', 'title': 'N-4', 'score': 0.007436374820247205}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-6.html', 'title': 'N-6', 'score': 0.007067531571211252}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-32.html', 'title': 'N-32', 'score': 0.0061683674084614}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-8.html', 'title': 'N-8', 'score': 0.005981202755875915}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-9.html', 'title': 'N-9', 'score': 0.005802767927053593}]
result = search.search('peach banana orange orange cherry cherry',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #1 checking search results for 'peach banana orange orange cherry cherry' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #1 checking search results for 'peach banana orange orange cherry cherry' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #2 checking search results for 'cherry kiwi papaya peach cherry tomato' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-935.html', 'title': 'N-935', 'score': 0.9998371968377247}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-667.html', 'title': 'N-667', 'score': 0.9998371968377247}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-529.html', 'title': 'N-529', 'score': 0.999756857740994}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-750.html', 'title': 'N-750', 'score': 0.9979153856286465}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-861.html', 'title': 'N-861', 'score': 0.9972494093904022}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-384.html', 'title': 'N-384', 'score': 0.9971923795477822}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-369.html', 'title': 'N-369', 'score': 0.9971863137485533}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-211.html', 'title': 'N-211', 'score': 0.9964222441883883}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-338.html', 'title': 'N-338', 'score': 0.9961603320819902}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-261.html', 'title': 'N-261', 'score': 0.9955157822232868}]
result = search.search('cherry kiwi papaya peach cherry tomato',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #2 checking search results for 'cherry kiwi papaya peach cherry tomato' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #2 checking search results for 'cherry kiwi papaya peach cherry tomato' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #3 checking search results for 'orange pear blueberry kiwi banana' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-235.html', 'title': 'N-235', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-2.html', 'title': 'N-2', 'score': 0.9980596237570685}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-951.html', 'title': 'N-951', 'score': 0.9979073760692476}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-947.html', 'title': 'N-947', 'score': 0.997294401544416}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-498.html', 'title': 'N-498', 'score': 0.9972145352808699}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-621.html', 'title': 'N-621', 'score': 0.9972051885579645}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-690.html', 'title': 'N-690', 'score': 0.9963146463217828}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-614.html', 'title': 'N-614', 'score': 0.9962064222737862}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-727.html', 'title': 'N-727', 'score': 0.9961979700290549}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-581.html', 'title': 'N-581', 'score': 0.9961341798458775}]
result = search.search('orange pear blueberry kiwi banana',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #3 checking search results for 'orange pear blueberry kiwi banana' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #3 checking search results for 'orange pear blueberry kiwi banana' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #4 checking search results for 'apricot pear kiwi apple' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-975.html', 'title': 'N-975', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-932.html', 'title': 'N-932', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-675.html', 'title': 'N-675', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-164.html', 'title': 'N-164', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-589.html', 'title': 'N-589', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-798.html', 'title': 'N-798', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-154.html', 'title': 'N-154', 'score': 0.9983404019762073}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-742.html', 'title': 'N-742', 'score': 0.9980336202419365}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-784.html', 'title': 'N-784', 'score': 0.9979312931704697}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-417.html', 'title': 'N-417', 'score': 0.9979088211387686}]
result = search.search('apricot pear kiwi apple',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #4 checking search results for 'apricot pear kiwi apple' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #4 checking search results for 'apricot pear kiwi apple' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #5 checking search results for 'orange banana papaya apple lime pear pear' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-916.html', 'title': 'N-916', 'score': 0.9961759265495311}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-395.html', 'title': 'N-395', 'score': 0.9948944098406522}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-285.html', 'title': 'N-285', 'score': 0.9947960752488945}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-20.html', 'title': 'N-20', 'score': 0.9941278033795311}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-291.html', 'title': 'N-291', 'score': 0.9937582326290662}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-795.html', 'title': 'N-795', 'score': 0.992880014708105}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-971.html', 'title': 'N-971', 'score': 0.9921152862391394}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-24.html', 'title': 'N-24', 'score': 0.9913583603698122}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-380.html', 'title': 'N-380', 'score': 0.9897278951744533}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-544.html', 'title': 'N-544', 'score': 0.9887345398617113}]
result = search.search('orange banana papaya apple lime pear pear',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #5 checking search results for 'orange banana papaya apple lime pear pear' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #5 checking search results for 'orange banana papaya apple lime pear pear' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #6 checking search results for 'coconut banana cherry apple banana tomato blueberry fig' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-723.html', 'title': 'N-723', 'score': 0.9932443952812221}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-349.html', 'title': 'N-349', 'score': 0.993162655435368}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-752.html', 'title': 'N-752', 'score': 0.9919929530743933}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-52.html', 'title': 'N-52', 'score': 0.9913647229065299}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-860.html', 'title': 'N-860', 'score': 0.9895391242225734}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-403.html', 'title': 'N-403', 'score': 0.9893491406975614}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-551.html', 'title': 'N-551', 'score': 0.9893448810661467}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-236.html', 'title': 'N-236', 'score': 0.9892106730949777}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-737.html', 'title': 'N-737', 'score': 0.9878608261586865}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-776.html', 'title': 'N-776', 'score': 0.9873402416587403}]
result = search.search('coconut banana cherry apple banana tomato blueberry fig',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #6 checking search results for 'coconut banana cherry apple banana tomato blueberry fig' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #6 checking search results for 'coconut banana cherry apple banana tomato blueberry fig' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #7 checking search results for 'lime fig blueberry pear coconut blueberry orange banana' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-151.html', 'title': 'N-151', 'score': 0.9914223220103329}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-432.html', 'title': 'N-432', 'score': 0.9883139856152774}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-404.html', 'title': 'N-404', 'score': 0.9877437548248583}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-313.html', 'title': 'N-313', 'score': 0.9876011090570687}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-340.html', 'title': 'N-340', 'score': 0.9865048084351793}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-456.html', 'title': 'N-456', 'score': 0.9856691208014765}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-57.html', 'title': 'N-57', 'score': 0.9849408315828434}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-27.html', 'title': 'N-27', 'score': 0.984750211952229}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-316.html', 'title': 'N-316', 'score': 0.983691932637333}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-512.html', 'title': 'N-512', 'score': 0.9833372825359846}]
result = search.search('lime fig blueberry pear coconut blueberry orange banana',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #7 checking search results for 'lime fig blueberry pear coconut blueberry orange banana' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #7 checking search results for 'lime fig blueberry pear coconut blueberry orange banana' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #8 checking search results for 'fig cherry fig pear fig cherry blueberry' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-992.html', 'title': 'N-992', 'score': 0.9990716870377327}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-175.html', 'title': 'N-175', 'score': 0.9946852277986667}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-134.html', 'title': 'N-134', 'score': 0.9913592355759863}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-959.html', 'title': 'N-959', 'score': 0.9912492190755243}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-260.html', 'title': 'N-260', 'score': 0.9903398061940067}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-774.html', 'title': 'N-774', 'score': 0.9900921078257001}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-471.html', 'title': 'N-471', 'score': 0.9898912678413674}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-467.html', 'title': 'N-467', 'score': 0.9895428800851969}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-970.html', 'title': 'N-970', 'score': 0.988890420772856}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-455.html', 'title': 'N-455', 'score': 0.9888130145535285}]
result = search.search('fig cherry fig pear fig cherry blueberry',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #8 checking search results for 'fig cherry fig pear fig cherry blueberry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #8 checking search results for 'fig cherry fig pear fig cherry blueberry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #9 checking search results for 'pear lime coconut kiwi fig banana orange tomato' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-148.html', 'title': 'N-148', 'score': 0.9942646607304325}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-93.html', 'title': 'N-93', 'score': 0.991723504415203}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-165.html', 'title': 'N-165', 'score': 0.9909842250759615}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-90.html', 'title': 'N-90', 'score': 0.989185661982469}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-154.html', 'title': 'N-154', 'score': 0.9882252728677314}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-241.html', 'title': 'N-241', 'score': 0.9882038959055104}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-530.html', 'title': 'N-530', 'score': 0.9881478902800994}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-682.html', 'title': 'N-682', 'score': 0.987850999837069}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-127.html', 'title': 'N-127', 'score': 0.9871533406805095}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-601.html', 'title': 'N-601', 'score': 0.9869918304468842}]
result = search.search('pear lime coconut kiwi fig banana orange tomato',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #9 checking search results for 'pear lime coconut kiwi fig banana orange tomato' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #9 checking search results for 'pear lime coconut kiwi fig banana orange tomato' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #10 checking search results for 'pear kiwi pear apple cherry cherry' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-529.html', 'title': 'N-529', 'score': 0.999833363688406}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-946.html', 'title': 'N-946', 'score': 0.9997777456644021}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-308.html', 'title': 'N-308', 'score': 0.999746883186766}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-243.html', 'title': 'N-243', 'score': 0.9974994229000705}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-449.html', 'title': 'N-449', 'score': 0.9971184804405393}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-285.html', 'title': 'N-285', 'score': 0.9969426952556174}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-990.html', 'title': 'N-990', 'score': 0.9956020384691644}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-337.html', 'title': 'N-337', 'score': 0.994858489937683}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-140.html', 'title': 'N-140', 'score': 0.9947063877551205}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-60.html', 'title': 'N-60', 'score': 0.9943535273906959}]
result = search.search('pear kiwi pear apple cherry cherry',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #10 checking search results for 'pear kiwi pear apple cherry cherry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #10 checking search results for 'pear kiwi pear apple cherry cherry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #11 checking search results for 'apple kiwi coconut peach lime banana kiwi' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-115.html', 'title': 'N-115', 'score': 0.9959618451326141}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-340.html', 'title': 'N-340', 'score': 0.9945286977453686}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-45.html', 'title': 'N-45', 'score': 0.994074809022604}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-916.html', 'title': 'N-916', 'score': 0.9928129132556859}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-938.html', 'title': 'N-938', 'score': 0.9912643463446537}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-83.html', 'title': 'N-83', 'score': 0.9908508036534406}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-55.html', 'title': 'N-55', 'score': 0.990332633009959}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-590.html', 'title': 'N-590', 'score': 0.9880345969432281}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-772.html', 'title': 'N-772', 'score': 0.9858138192729395}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-957.html', 'title': 'N-957', 'score': 0.9854050093235533}]
result = search.search('apple kiwi coconut peach lime banana kiwi',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #11 checking search results for 'apple kiwi coconut peach lime banana kiwi' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #11 checking search results for 'apple kiwi coconut peach lime banana kiwi' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #12 checking search results for 'banana blueberry peach cherry fig papaya kiwi cherry' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-530.html', 'title': 'N-530', 'score': 0.9938082200453255}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-429.html', 'title': 'N-429', 'score': 0.9927834619008618}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-384.html', 'title': 'N-384', 'score': 0.9922741348376491}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-336.html', 'title': 'N-336', 'score': 0.9884913486603858}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-271.html', 'title': 'N-271', 'score': 0.9884601404485497}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-482.html', 'title': 'N-482', 'score': 0.9817780205744313}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-165.html', 'title': 'N-165', 'score': 0.9811676385736691}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-849.html', 'title': 'N-849', 'score': 0.9808558726711025}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-286.html', 'title': 'N-286', 'score': 0.9799722180646969}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-417.html', 'title': 'N-417', 'score': 0.9794065345764472}]
result = search.search('banana blueberry peach cherry fig papaya kiwi cherry',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #12 checking search results for 'banana blueberry peach cherry fig papaya kiwi cherry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #12 checking search results for 'banana blueberry peach cherry fig papaya kiwi cherry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #13 checking search results for 'tomato apple banana lime kiwi banana pear coconut' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-52.html', 'title': 'N-52', 'score': 0.9884854421366616}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-261.html', 'title': 'N-261', 'score': 0.9865744491949408}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-386.html', 'title': 'N-386', 'score': 0.9855403256892037}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-475.html', 'title': 'N-475', 'score': 0.9852265353051222}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-991.html', 'title': 'N-991', 'score': 0.9850552692598171}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-315.html', 'title': 'N-315', 'score': 0.9849021718701465}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-236.html', 'title': 'N-236', 'score': 0.9840700805095552}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-585.html', 'title': 'N-585', 'score': 0.9831975711415464}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-798.html', 'title': 'N-798', 'score': 0.9827764730722175}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-123.html', 'title': 'N-123', 'score': 0.982567343853556}]
result = search.search('tomato apple banana lime kiwi banana pear coconut',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #13 checking search results for 'tomato apple banana lime kiwi banana pear coconut' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #13 checking search results for 'tomato apple banana lime kiwi banana pear coconut' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #14 checking search results for 'orange fig orange coconut papaya fig fig tomato' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-12.html', 'title': 'N-12', 'score': 0.9998207684160371}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-390.html', 'title': 'N-390', 'score': 0.9997767431939288}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-846.html', 'title': 'N-846', 'score': 0.9981717788137303}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-557.html', 'title': 'N-557', 'score': 0.9924702365631324}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-197.html', 'title': 'N-197', 'score': 0.9906538668109317}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-237.html', 'title': 'N-237', 'score': 0.9893488773203064}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-424.html', 'title': 'N-424', 'score': 0.9886886146909102}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-525.html', 'title': 'N-525', 'score': 0.988679839617555}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-94.html', 'title': 'N-94', 'score': 0.9886677990455635}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-482.html', 'title': 'N-482', 'score': 0.9880273019709548}]
result = search.search('orange fig orange coconut papaya fig fig tomato',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #14 checking search results for 'orange fig orange coconut papaya fig fig tomato' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #14 checking search results for 'orange fig orange coconut papaya fig fig tomato' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #15 checking search results for 'pear fig fig orange fig fig tomato peach' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-500.html', 'title': 'N-500', 'score': 0.9955475316422807}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-875.html', 'title': 'N-875', 'score': 0.9952504793806289}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-979.html', 'title': 'N-979', 'score': 0.9927358358949362}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-792.html', 'title': 'N-792', 'score': 0.9911793834745652}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-991.html', 'title': 'N-991', 'score': 0.9900757404506124}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-924.html', 'title': 'N-924', 'score': 0.9862000055966332}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-710.html', 'title': 'N-710', 'score': 0.9834015496077163}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-904.html', 'title': 'N-904', 'score': 0.9832029415094532}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-868.html', 'title': 'N-868', 'score': 0.9826030969513414}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-959.html', 'title': 'N-959', 'score': 0.9822455835233918}]
result = search.search('pear fig fig orange fig fig tomato peach',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #15 checking search results for 'pear fig fig orange fig fig tomato peach' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #15 checking search results for 'pear fig fig orange fig fig tomato peach' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #16 checking search results for 'orange orange lime papaya kiwi papaya orange' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-370.html', 'title': 'N-370', 'score': 0.9994992594681001}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-107.html', 'title': 'N-107', 'score': 0.9973238593063561}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-294.html', 'title': 'N-294', 'score': 0.9965844539515988}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-953.html', 'title': 'N-953', 'score': 0.9954124038788983}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-187.html', 'title': 'N-187', 'score': 0.9949922306559554}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-15.html', 'title': 'N-15', 'score': 0.9934749878722073}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-570.html', 'title': 'N-570', 'score': 0.9932213864232182}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-897.html', 'title': 'N-897', 'score': 0.9911772516981023}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-267.html', 'title': 'N-267', 'score': 0.9906786669754142}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-309.html', 'title': 'N-309', 'score': 0.9906561270159008}]
result = search.search('orange orange lime papaya kiwi papaya orange',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #16 checking search results for 'orange orange lime papaya kiwi papaya orange' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #16 checking search results for 'orange orange lime papaya kiwi papaya orange' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #17 checking search results for 'banana apple apple orange apple' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-374.html', 'title': 'N-374', 'score': 0.9999933789217784}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-476.html', 'title': 'N-476', 'score': 0.9994117229355708}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-255.html', 'title': 'N-255', 'score': 0.9991773400279641}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-536.html', 'title': 'N-536', 'score': 0.9991259377535907}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-559.html', 'title': 'N-559', 'score': 0.9988978410380117}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-173.html', 'title': 'N-173', 'score': 0.9988079617259806}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-319.html', 'title': 'N-319', 'score': 0.9987608441605124}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-288.html', 'title': 'N-288', 'score': 0.9979602720677537}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-921.html', 'title': 'N-921', 'score': 0.9977625688231642}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-758.html', 'title': 'N-758', 'score': 0.9975608655535001}]
result = search.search('banana apple apple orange apple',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #17 checking search results for 'banana apple apple orange apple' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #17 checking search results for 'banana apple apple orange apple' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #18 checking search results for 'lime coconut lime banana kiwi coconut cherry' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-25.html', 'title': 'N-25', 'score': 0.999841003429065}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-372.html', 'title': 'N-372', 'score': 0.9981420147339961}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-999.html', 'title': 'N-999', 'score': 0.9976904737804123}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-619.html', 'title': 'N-619', 'score': 0.9944577088115893}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-190.html', 'title': 'N-190', 'score': 0.9931853603745036}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-587.html', 'title': 'N-587', 'score': 0.9929945344344911}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-812.html', 'title': 'N-812', 'score': 0.992882616294252}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-635.html', 'title': 'N-635', 'score': 0.992324184561492}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-884.html', 'title': 'N-884', 'score': 0.9919805506076195}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-679.html', 'title': 'N-679', 'score': 0.9914112383791273}]
result = search.search('lime coconut lime banana kiwi coconut cherry',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #18 checking search results for 'lime coconut lime banana kiwi coconut cherry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #18 checking search results for 'lime coconut lime banana kiwi coconut cherry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #19 checking search results for 'pear kiwi peach kiwi blueberry blueberry cherry tomato' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-949.html', 'title': 'N-949', 'score': 0.9947120915035141}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-400.html', 'title': 'N-400', 'score': 0.9941161645484328}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-468.html', 'title': 'N-468', 'score': 0.9937608888717799}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-376.html', 'title': 'N-376', 'score': 0.9923933801761059}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-352.html', 'title': 'N-352', 'score': 0.9893931425941778}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-559.html', 'title': 'N-559', 'score': 0.9890901076291392}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-746.html', 'title': 'N-746', 'score': 0.9886798971145724}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-583.html', 'title': 'N-583', 'score': 0.9882458140262697}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-57.html', 'title': 'N-57', 'score': 0.9881078768328163}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-918.html', 'title': 'N-918', 'score': 0.9879119676842275}]
result = search.search('pear kiwi peach kiwi blueberry blueberry cherry tomato',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #19 checking search results for 'pear kiwi peach kiwi blueberry blueberry cherry tomato' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #19 checking search results for 'pear kiwi peach kiwi blueberry blueberry cherry tomato' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #20 checking search results for 'peach lime tomato fig kiwi banana blueberry apple' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-656.html', 'title': 'N-656', 'score': 0.9958042858257203}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-859.html', 'title': 'N-859', 'score': 0.9945531574063857}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-286.html', 'title': 'N-286', 'score': 0.9909717692444001}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-387.html', 'title': 'N-387', 'score': 0.9909687062789898}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-154.html', 'title': 'N-154', 'score': 0.9909488468670964}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-754.html', 'title': 'N-754', 'score': 0.9909155421469628}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-967.html', 'title': 'N-967', 'score': 0.9908439606087448}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-152.html', 'title': 'N-152', 'score': 0.9899860484504993}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-882.html', 'title': 'N-882', 'score': 0.9891644723239469}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-922.html', 'title': 'N-922', 'score': 0.9891099695611104}]
result = search.search('peach lime tomato fig kiwi banana blueberry apple',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #20 checking search results for 'peach lime tomato fig kiwi banana blueberry apple' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #20 checking search results for 'peach lime tomato fig kiwi banana blueberry apple' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #21 checking search results for 'fig apricot blueberry coconut blueberry apple' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-92.html', 'title': 'N-92', 'score': 0.9997873336580225}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-483.html', 'title': 'N-483', 'score': 0.997479710926509}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-975.html', 'title': 'N-975', 'score': 0.9964019027035738}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-460.html', 'title': 'N-460', 'score': 0.9949283428434557}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-607.html', 'title': 'N-607', 'score': 0.9948523058704899}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-538.html', 'title': 'N-538', 'score': 0.9931953574890054}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-279.html', 'title': 'N-279', 'score': 0.9901646416506096}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-448.html', 'title': 'N-448', 'score': 0.9889227608231859}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-111.html', 'title': 'N-111', 'score': 0.9882016149106247}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-404.html', 'title': 'N-404', 'score': 0.9881832185112024}]
result = search.search('fig apricot blueberry coconut blueberry apple',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #21 checking search results for 'fig apricot blueberry coconut blueberry apple' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #21 checking search results for 'fig apricot blueberry coconut blueberry apple' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #22 checking search results for 'kiwi peach pear peach orange pear apple' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-430.html', 'title': 'N-430', 'score': 0.9954646008787736}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-438.html', 'title': 'N-438', 'score': 0.9954289513268344}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-997.html', 'title': 'N-997', 'score': 0.9943627978710236}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-917.html', 'title': 'N-917', 'score': 0.9933547436492327}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-847.html', 'title': 'N-847', 'score': 0.9928308597518128}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-289.html', 'title': 'N-289', 'score': 0.9922397077963083}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-24.html', 'title': 'N-24', 'score': 0.992133758456416}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-77.html', 'title': 'N-77', 'score': 0.9915869586568337}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-920.html', 'title': 'N-920', 'score': 0.9895172456414023}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-407.html', 'title': 'N-407', 'score': 0.9884694598282053}]
result = search.search('kiwi peach pear peach orange pear apple',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #22 checking search results for 'kiwi peach pear peach orange pear apple' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #22 checking search results for 'kiwi peach pear peach orange pear apple' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #23 checking search results for 'papaya banana coconut fig peach cherry' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-662.html', 'title': 'N-662', 'score': 0.998312431412449}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-647.html', 'title': 'N-647', 'score': 0.9972790795514042}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-633.html', 'title': 'N-633', 'score': 0.9951014419501223}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-258.html', 'title': 'N-258', 'score': 0.9939137606287758}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-72.html', 'title': 'N-72', 'score': 0.9935351277816904}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-340.html', 'title': 'N-340', 'score': 0.9934540080800414}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-183.html', 'title': 'N-183', 'score': 0.9934115338310106}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-469.html', 'title': 'N-469', 'score': 0.9923417950893547}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-7.html', 'title': 'N-7', 'score': 0.9921824278544361}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-938.html', 'title': 'N-938', 'score': 0.9916588499278854}]
result = search.search('papaya banana coconut fig peach cherry',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #23 checking search results for 'papaya banana coconut fig peach cherry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #23 checking search results for 'papaya banana coconut fig peach cherry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #24 checking search results for 'pear apricot kiwi kiwi lime blueberry orange apricot' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-461.html', 'title': 'N-461', 'score': 0.9949413234062244}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-88.html', 'title': 'N-88', 'score': 0.9926361661455507}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-686.html', 'title': 'N-686', 'score': 0.9883084299580132}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-774.html', 'title': 'N-774', 'score': 0.9872609634394711}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-567.html', 'title': 'N-567', 'score': 0.9871934476877116}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-688.html', 'title': 'N-688', 'score': 0.9867136611644513}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-188.html', 'title': 'N-188', 'score': 0.9860479810718286}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-258.html', 'title': 'N-258', 'score': 0.9844839601443802}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-440.html', 'title': 'N-440', 'score': 0.9842650370716726}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-45.html', 'title': 'N-45', 'score': 0.9831493708069982}]
result = search.search('pear apricot kiwi kiwi lime blueberry orange apricot',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #24 checking search results for 'pear apricot kiwi kiwi lime blueberry orange apricot' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #24 checking search results for 'pear apricot kiwi kiwi lime blueberry orange apricot' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #25 checking search results for 'peach fig banana coconut' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-154.html', 'title': 'N-154', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-207.html', 'title': 'N-207', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-199.html', 'title': 'N-199', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-225.html', 'title': 'N-225', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-847.html', 'title': 'N-847', 'score': 0.9979986955288125}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-662.html', 'title': 'N-662', 'score': 0.9979721560834853}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-340.html', 'title': 'N-340', 'score': 0.9979147873374484}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-72.html', 'title': 'N-72', 'score': 0.997353875227539}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-239.html', 'title': 'N-239', 'score': 0.9973490607489824}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-647.html', 'title': 'N-647', 'score': 0.9973027098040418}]
result = search.search('peach fig banana coconut',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #25 checking search results for 'peach fig banana coconut' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #25 checking search results for 'peach fig banana coconut' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #26 checking search results for 'orange coconut coconut kiwi papaya orange coconut apricot' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-977.html', 'title': 'N-977', 'score': 0.9958549946143256}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-698.html', 'title': 'N-698', 'score': 0.9949450815310801}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-839.html', 'title': 'N-839', 'score': 0.9917753083030716}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-96.html', 'title': 'N-96', 'score': 0.9908667512489739}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-875.html', 'title': 'N-875', 'score': 0.9894932532689602}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-529.html', 'title': 'N-529', 'score': 0.9894042113154534}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-897.html', 'title': 'N-897', 'score': 0.9888823076794984}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-486.html', 'title': 'N-486', 'score': 0.9882786230207109}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-392.html', 'title': 'N-392', 'score': 0.9878151731445146}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-565.html', 'title': 'N-565', 'score': 0.987325444903715}]
result = search.search('orange coconut coconut kiwi papaya orange coconut apricot',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #26 checking search results for 'orange coconut coconut kiwi papaya orange coconut apricot' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #26 checking search results for 'orange coconut coconut kiwi papaya orange coconut apricot' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #27 checking search results for 'kiwi pear coconut lime pear cherry pear tomato' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-843.html', 'title': 'N-843', 'score': 0.9941079250043515}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-769.html', 'title': 'N-769', 'score': 0.9940503247858967}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-288.html', 'title': 'N-288', 'score': 0.9932760823673106}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-557.html', 'title': 'N-557', 'score': 0.993002002510795}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-41.html', 'title': 'N-41', 'score': 0.9906115617057621}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-144.html', 'title': 'N-144', 'score': 0.9905426150938633}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-953.html', 'title': 'N-953', 'score': 0.9893206307007427}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-873.html', 'title': 'N-873', 'score': 0.9817058318972982}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-22.html', 'title': 'N-22', 'score': 0.9779240927938737}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-664.html', 'title': 'N-664', 'score': 0.9772318404488681}]
result = search.search('kiwi pear coconut lime pear cherry pear tomato',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #27 checking search results for 'kiwi pear coconut lime pear cherry pear tomato' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #27 checking search results for 'kiwi pear coconut lime pear cherry pear tomato' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #28 checking search results for 'fig lime kiwi papaya papaya' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-872.html', 'title': 'N-872', 'score': 0.9999141305247485}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-474.html', 'title': 'N-474', 'score': 0.9997442581533955}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-41.html', 'title': 'N-41', 'score': 0.9995867837698157}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-262.html', 'title': 'N-262', 'score': 0.9995102037644914}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-158.html', 'title': 'N-158', 'score': 0.9979472005233558}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-551.html', 'title': 'N-551', 'score': 0.9978148833800032}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-430.html', 'title': 'N-430', 'score': 0.9977553367452}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-512.html', 'title': 'N-512', 'score': 0.9975965137356725}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-26.html', 'title': 'N-26', 'score': 0.9968227314224708}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-826.html', 'title': 'N-826', 'score': 0.9962857223119473}]
result = search.search('fig lime kiwi papaya papaya',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #28 checking search results for 'fig lime kiwi papaya papaya' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #28 checking search results for 'fig lime kiwi papaya papaya' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #29 checking search results for 'fig pear apricot lime kiwi apricot cherry fig' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-364.html', 'title': 'N-364', 'score': 0.9998523261294014}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-676.html', 'title': 'N-676', 'score': 0.9952227056602122}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-991.html', 'title': 'N-991', 'score': 0.9898235443924501}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-180.html', 'title': 'N-180', 'score': 0.9891467484222297}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html', 'title': 'N-0', 'score': 0.9891331351215308}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-470.html', 'title': 'N-470', 'score': 0.9881617741477784}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-940.html', 'title': 'N-940', 'score': 0.9872591831770787}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-386.html', 'title': 'N-386', 'score': 0.9861846805527409}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-958.html', 'title': 'N-958', 'score': 0.986016711125148}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-484.html', 'title': 'N-484', 'score': 0.985841255729243}]
result = search.search('fig pear apricot lime kiwi apricot cherry fig',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #29 checking search results for 'fig pear apricot lime kiwi apricot cherry fig' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #29 checking search results for 'fig pear apricot lime kiwi apricot cherry fig' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #30 checking search results for 'lime cherry apricot fig fig banana fig banana' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-390.html', 'title': 'N-390', 'score': 0.9997379931481876}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-792.html', 'title': 'N-792', 'score': 0.992859986397252}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-224.html', 'title': 'N-224', 'score': 0.9912478780357282}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-897.html', 'title': 'N-897', 'score': 0.9908422196290017}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-69.html', 'title': 'N-69', 'score': 0.989391691689772}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-565.html', 'title': 'N-565', 'score': 0.989072256645972}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-424.html', 'title': 'N-424', 'score': 0.9883621746669905}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-193.html', 'title': 'N-193', 'score': 0.9871373528647782}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-195.html', 'title': 'N-195', 'score': 0.9867241158763693}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-118.html', 'title': 'N-118', 'score': 0.9860749885722455}]
result = search.search('lime cherry apricot fig fig banana fig banana',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #30 checking search results for 'lime cherry apricot fig fig banana fig banana' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #30 checking search results for 'lime cherry apricot fig fig banana fig banana' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #31 checking search results for 'blueberry fig blueberry cherry pear apricot' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-680.html', 'title': 'N-680', 'score': 0.9997526352836044}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-483.html', 'title': 'N-483', 'score': 0.9974840998379617}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-518.html', 'title': 'N-518', 'score': 0.9969521368705481}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-57.html', 'title': 'N-57', 'score': 0.9957088231304644}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-903.html', 'title': 'N-903', 'score': 0.9949711759451741}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-977.html', 'title': 'N-977', 'score': 0.9931674139121699}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-798.html', 'title': 'N-798', 'score': 0.9924308292311104}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-486.html', 'title': 'N-486', 'score': 0.9922364505835438}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-27.html', 'title': 'N-27', 'score': 0.9900073895194367}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-404.html', 'title': 'N-404', 'score': 0.9884126391450292}]
result = search.search('blueberry fig blueberry cherry pear apricot',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #31 checking search results for 'blueberry fig blueberry cherry pear apricot' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #31 checking search results for 'blueberry fig blueberry cherry pear apricot' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #32 checking search results for 'pear banana papaya kiwi banana' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-750.html', 'title': 'N-750', 'score': 0.9996079558436908}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-645.html', 'title': 'N-645', 'score': 0.9995715016555403}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-347.html', 'title': 'N-347', 'score': 0.9995010494324508}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-116.html', 'title': 'N-116', 'score': 0.9993688210614312}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-176.html', 'title': 'N-176', 'score': 0.9992645444278956}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-179.html', 'title': 'N-179', 'score': 0.9977342773635275}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-386.html', 'title': 'N-386', 'score': 0.997628906528394}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-109.html', 'title': 'N-109', 'score': 0.9967821792736571}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-341.html', 'title': 'N-341', 'score': 0.9967613806683053}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-43.html', 'title': 'N-43', 'score': 0.9963766810526661}]
result = search.search('pear banana papaya kiwi banana',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #32 checking search results for 'pear banana papaya kiwi banana' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #32 checking search results for 'pear banana papaya kiwi banana' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #33 checking search results for 'orange lime cherry lime apricot peach' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-119.html', 'title': 'N-119', 'score': 0.9977608994372988}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-231.html', 'title': 'N-231', 'score': 0.9973007492129367}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-559.html', 'title': 'N-559', 'score': 0.9962159209749416}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-707.html', 'title': 'N-707', 'score': 0.995553743013535}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-949.html', 'title': 'N-949', 'score': 0.9952543156750023}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-542.html', 'title': 'N-542', 'score': 0.9949533994887878}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-72.html', 'title': 'N-72', 'score': 0.9939398588438195}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-86.html', 'title': 'N-86', 'score': 0.9938459693803134}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-812.html', 'title': 'N-812', 'score': 0.9936481499816646}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-100.html', 'title': 'N-100', 'score': 0.9935730217605554}]
result = search.search('orange lime cherry lime apricot peach',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #33 checking search results for 'orange lime cherry lime apricot peach' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #33 checking search results for 'orange lime cherry lime apricot peach' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #34 checking search results for 'peach fig pear orange orange pear' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-428.html', 'title': 'N-428', 'score': 0.9974185286609062}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-763.html', 'title': 'N-763', 'score': 0.9972044049781289}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-509.html', 'title': 'N-509', 'score': 0.9968523256781039}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-925.html', 'title': 'N-925', 'score': 0.9958072391816692}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-690.html', 'title': 'N-690', 'score': 0.995803967480139}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-641.html', 'title': 'N-641', 'score': 0.995779860194269}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-378.html', 'title': 'N-378', 'score': 0.9956240484647029}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-581.html', 'title': 'N-581', 'score': 0.9952821075726259}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-951.html', 'title': 'N-951', 'score': 0.9945980132516061}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-855.html', 'title': 'N-855', 'score': 0.9945689218424242}]
result = search.search('peach fig pear orange orange pear',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #34 checking search results for 'peach fig pear orange orange pear' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #34 checking search results for 'peach fig pear orange orange pear' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #35 checking search results for 'fig pear apple apricot apricot apricot' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-715.html', 'title': 'N-715', 'score': 0.9993201678498014}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-214.html', 'title': 'N-214', 'score': 0.9991572087737247}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-663.html', 'title': 'N-663', 'score': 0.9990739252287614}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-345.html', 'title': 'N-345', 'score': 0.9952298989589651}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-845.html', 'title': 'N-845', 'score': 0.9942650680243467}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-540.html', 'title': 'N-540', 'score': 0.9923489032959714}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-445.html', 'title': 'N-445', 'score': 0.9923276252527945}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-902.html', 'title': 'N-902', 'score': 0.9923276252527945}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-570.html', 'title': 'N-570', 'score': 0.9902152732510068}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-796.html', 'title': 'N-796', 'score': 0.9892954829919378}]
result = search.search('fig pear apple apricot apricot apricot',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #35 checking search results for 'fig pear apple apricot apricot apricot' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #35 checking search results for 'fig pear apple apricot apricot apricot' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #36 checking search results for 'blueberry peach coconut pear orange kiwi pear cherry' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-72.html', 'title': 'N-72', 'score': 0.9964102395292339}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-586.html', 'title': 'N-586', 'score': 0.9939677045870225}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-383.html', 'title': 'N-383', 'score': 0.9933927486783075}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-344.html', 'title': 'N-344', 'score': 0.9911735425481966}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-664.html', 'title': 'N-664', 'score': 0.9909576272126979}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-41.html', 'title': 'N-41', 'score': 0.989573690030213}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-144.html', 'title': 'N-144', 'score': 0.9879181215434729}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-398.html', 'title': 'N-398', 'score': 0.9873309437241273}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-887.html', 'title': 'N-887', 'score': 0.9862118632328107}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-814.html', 'title': 'N-814', 'score': 0.9843991333143142}]
result = search.search('blueberry peach coconut pear orange kiwi pear cherry',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #36 checking search results for 'blueberry peach coconut pear orange kiwi pear cherry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #36 checking search results for 'blueberry peach coconut pear orange kiwi pear cherry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #37 checking search results for 'kiwi coconut apple cherry blueberry cherry peach lime' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-935.html', 'title': 'N-935', 'score': 0.9908696866677643}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-123.html', 'title': 'N-123', 'score': 0.9899751031501263}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-449.html', 'title': 'N-449', 'score': 0.987314640589402}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-530.html', 'title': 'N-530', 'score': 0.9871319657945196}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-155.html', 'title': 'N-155', 'score': 0.9869880862994629}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-902.html', 'title': 'N-902', 'score': 0.9865695956791842}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-250.html', 'title': 'N-250', 'score': 0.9856884807887646}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-286.html', 'title': 'N-286', 'score': 0.9850593968840711}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-447.html', 'title': 'N-447', 'score': 0.9838307040536379}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-900.html', 'title': 'N-900', 'score': 0.9837845886392178}]
result = search.search('kiwi coconut apple cherry blueberry cherry peach lime',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #37 checking search results for 'kiwi coconut apple cherry blueberry cherry peach lime' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #37 checking search results for 'kiwi coconut apple cherry blueberry cherry peach lime' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #38 checking search results for 'coconut banana peach coconut banana apricot papaya kiwi' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-971.html', 'title': 'N-971', 'score': 0.9949427350500749}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-913.html', 'title': 'N-913', 'score': 0.9939543387816322}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-839.html', 'title': 'N-839', 'score': 0.9935651060775357}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-43.html', 'title': 'N-43', 'score': 0.9925685033705588}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-522.html', 'title': 'N-522', 'score': 0.9918441157430689}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-367.html', 'title': 'N-367', 'score': 0.9907077532218073}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-438.html', 'title': 'N-438', 'score': 0.9904816916517011}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-118.html', 'title': 'N-118', 'score': 0.9897843755693327}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-69.html', 'title': 'N-69', 'score': 0.9876467842589818}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-452.html', 'title': 'N-452', 'score': 0.9858087448275878}]
result = search.search('coconut banana peach coconut banana apricot papaya kiwi',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #38 checking search results for 'coconut banana peach coconut banana apricot papaya kiwi' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #38 checking search results for 'coconut banana peach coconut banana apricot papaya kiwi' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #39 checking search results for 'lime papaya coconut blueberry' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-317.html', 'title': 'N-317', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-935.html', 'title': 'N-935', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-281.html', 'title': 'N-281', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-403.html', 'title': 'N-403', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-53.html', 'title': 'N-53', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-731.html', 'title': 'N-731', 'score': 0.9988073737776327}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-957.html', 'title': 'N-957', 'score': 0.9987979376180459}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-530.html', 'title': 'N-530', 'score': 0.9976826566190012}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-394.html', 'title': 'N-394', 'score': 0.997501291906714}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-590.html', 'title': 'N-590', 'score': 0.9972155100666359}]
result = search.search('lime papaya coconut blueberry',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #39 checking search results for 'lime papaya coconut blueberry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #39 checking search results for 'lime papaya coconut blueberry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #40 checking search results for 'orange kiwi cherry apricot orange pear blueberry' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-311.html', 'title': 'N-311', 'score': 0.9963060203402133}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-826.html', 'title': 'N-826', 'score': 0.9959919455752582}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-679.html', 'title': 'N-679', 'score': 0.993570605010645}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-118.html', 'title': 'N-118', 'score': 0.993126338267698}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-745.html', 'title': 'N-745', 'score': 0.990903113461476}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-314.html', 'title': 'N-314', 'score': 0.9897923593487604}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-844.html', 'title': 'N-844', 'score': 0.9884376031953999}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-179.html', 'title': 'N-179', 'score': 0.9882270974803387}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-435.html', 'title': 'N-435', 'score': 0.9865417000444882}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-443.html', 'title': 'N-443', 'score': 0.9864212485175561}]
result = search.search('orange kiwi cherry apricot orange pear blueberry',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #40 checking search results for 'orange kiwi cherry apricot orange pear blueberry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #40 checking search results for 'orange kiwi cherry apricot orange pear blueberry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #41 checking search results for 'fig apple apricot orange tomato apricot pear' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-258.html', 'title': 'N-258', 'score': 0.9946738703449893}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-845.html', 'title': 'N-845', 'score': 0.9944367878115666}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-97.html', 'title': 'N-97', 'score': 0.9927125298129733}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-214.html', 'title': 'N-214', 'score': 0.9922754007970945}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-200.html', 'title': 'N-200', 'score': 0.9922349043035573}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-188.html', 'title': 'N-188', 'score': 0.9921338863574986}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-43.html', 'title': 'N-43', 'score': 0.9913169970156055}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-349.html', 'title': 'N-349', 'score': 0.9899131789061882}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-337.html', 'title': 'N-337', 'score': 0.989815241220383}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-849.html', 'title': 'N-849', 'score': 0.9891022995797484}]
result = search.search('fig apple apricot orange tomato apricot pear',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #41 checking search results for 'fig apple apricot orange tomato apricot pear' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #41 checking search results for 'fig apple apricot orange tomato apricot pear' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #42 checking search results for 'papaya peach pear apricot tomato papaya' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-121.html', 'title': 'N-121', 'score': 0.9998777713994682}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-230.html', 'title': 'N-230', 'score': 0.9981849607413876}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-728.html', 'title': 'N-728', 'score': 0.998067909145706}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-789.html', 'title': 'N-789', 'score': 0.9978431693577524}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-652.html', 'title': 'N-652', 'score': 0.9977026918529891}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-826.html', 'title': 'N-826', 'score': 0.9970809413491345}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-83.html', 'title': 'N-83', 'score': 0.9950790320333286}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-785.html', 'title': 'N-785', 'score': 0.9950035053628657}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-304.html', 'title': 'N-304', 'score': 0.9948994915606919}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-975.html', 'title': 'N-975', 'score': 0.9942309590155869}]
result = search.search('papaya peach pear apricot tomato papaya',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #42 checking search results for 'papaya peach pear apricot tomato papaya' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #42 checking search results for 'papaya peach pear apricot tomato papaya' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #43 checking search results for 'papaya blueberry papaya cherry fig lime fig' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-248.html', 'title': 'N-248', 'score': 0.9998716455733286}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-774.html', 'title': 'N-774', 'score': 0.9972043319393507}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-302.html', 'title': 'N-302', 'score': 0.9929611377585409}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-593.html', 'title': 'N-593', 'score': 0.9923859041958614}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-175.html', 'title': 'N-175', 'score': 0.9914021812160444}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-186.html', 'title': 'N-186', 'score': 0.9910916087027869}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-713.html', 'title': 'N-713', 'score': 0.990068084200549}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-730.html', 'title': 'N-730', 'score': 0.9900424987589712}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-479.html', 'title': 'N-479', 'score': 0.9893616125174085}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-843.html', 'title': 'N-843', 'score': 0.989350898148064}]
result = search.search('papaya blueberry papaya cherry fig lime fig',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #43 checking search results for 'papaya blueberry papaya cherry fig lime fig' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #43 checking search results for 'papaya blueberry papaya cherry fig lime fig' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #44 checking search results for 'fig lime kiwi banana papaya pear banana cherry' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-176.html', 'title': 'N-176', 'score': 0.9947514762174768}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-43.html', 'title': 'N-43', 'score': 0.9920447112789137}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-17.html', 'title': 'N-17', 'score': 0.9916720421192761}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-109.html', 'title': 'N-109', 'score': 0.9912844242842672}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-179.html', 'title': 'N-179', 'score': 0.9910402214702936}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-382.html', 'title': 'N-382', 'score': 0.988847887363261}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-397.html', 'title': 'N-397', 'score': 0.9877541845967596}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-386.html', 'title': 'N-386', 'score': 0.9850659092545698}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-937.html', 'title': 'N-937', 'score': 0.9841314881438983}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-394.html', 'title': 'N-394', 'score': 0.9839443312643495}]
result = search.search('fig lime kiwi banana papaya pear banana cherry',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #44 checking search results for 'fig lime kiwi banana papaya pear banana cherry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #44 checking search results for 'fig lime kiwi banana papaya pear banana cherry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #45 checking search results for 'cherry banana blueberry peach papaya fig fig' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-268.html', 'title': 'N-268', 'score': 0.9954958616249829}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-455.html', 'title': 'N-455', 'score': 0.9943687100497889}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-464.html', 'title': 'N-464', 'score': 0.9941019178846191}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-443.html', 'title': 'N-443', 'score': 0.9933861637158724}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-586.html', 'title': 'N-586', 'score': 0.9914770158838336}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-559.html', 'title': 'N-559', 'score': 0.991269569456389}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-710.html', 'title': 'N-710', 'score': 0.9909908017455449}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-897.html', 'title': 'N-897', 'score': 0.9906508526317289}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-115.html', 'title': 'N-115', 'score': 0.9903936359196645}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-964.html', 'title': 'N-964', 'score': 0.9902917529859009}]
result = search.search('cherry banana blueberry peach papaya fig fig',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #45 checking search results for 'cherry banana blueberry peach papaya fig fig' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #45 checking search results for 'cherry banana blueberry peach papaya fig fig' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #46 checking search results for 'cherry apricot fig pear blueberry orange orange' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-311.html', 'title': 'N-311', 'score': 0.9963090289488713}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-826.html', 'title': 'N-826', 'score': 0.995405743338906}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-7.html', 'title': 'N-7', 'score': 0.9913826803969552}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-230.html', 'title': 'N-230', 'score': 0.9885487612971798}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-435.html', 'title': 'N-435', 'score': 0.9865651269455369}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-844.html', 'title': 'N-844', 'score': 0.9856018404566069}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-107.html', 'title': 'N-107', 'score': 0.9854803434635174}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-620.html', 'title': 'N-620', 'score': 0.9850922556192016}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-746.html', 'title': 'N-746', 'score': 0.985000978111584}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-880.html', 'title': 'N-880', 'score': 0.9834146009196452}]
result = search.search('cherry apricot fig pear blueberry orange orange',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #46 checking search results for 'cherry apricot fig pear blueberry orange orange' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #46 checking search results for 'cherry apricot fig pear blueberry orange orange' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


output.close()
success_output.close()
