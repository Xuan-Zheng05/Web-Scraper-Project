
import testingtools
import crawler
import searchdata
import search
output = open('fruits5-search-failed.txt', 'w')
success_output = open('fruits5-search-passed.txt', 'w')

#Performing crawl starting at seed http://people.scs.carleton.ca/~davidmckenney/fruits5/N-0.html
crawler.crawl('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-0.html')
#Test #0 checking search results for 'blueberry fig coconut blueberry apple blueberry' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-735.html', 'title': 'N-735', 'score': 0.9997993238979903}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-175.html', 'title': 'N-175', 'score': 0.9995622009168911}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-489.html', 'title': 'N-489', 'score': 0.9991399311711638}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-707.html', 'title': 'N-707', 'score': 0.9956504955381433}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-597.html', 'title': 'N-597', 'score': 0.9953417155364362}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-181.html', 'title': 'N-181', 'score': 0.9942103133332472}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-937.html', 'title': 'N-937', 'score': 0.9940010870766753}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-311.html', 'title': 'N-311', 'score': 0.9934496048448963}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-494.html', 'title': 'N-494', 'score': 0.9929039023420044}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-711.html', 'title': 'N-711', 'score': 0.9919860616769056}]
result = search.search('blueberry fig coconut blueberry apple blueberry',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #0 checking search results for 'blueberry fig coconut blueberry apple blueberry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #0 checking search results for 'blueberry fig coconut blueberry apple blueberry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #1 checking search results for 'cherry lime cherry apple tomato papaya' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-869.html', 'title': 'N-869', 'score': 0.9998998561340877}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-535.html', 'title': 'N-535', 'score': 0.9998285380496176}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-568.html', 'title': 'N-568', 'score': 0.9998101775276027}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-908.html', 'title': 'N-908', 'score': 0.9997673893456083}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-96.html', 'title': 'N-96', 'score': 0.9997403492928861}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-208.html', 'title': 'N-208', 'score': 0.9981428809269294}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-353.html', 'title': 'N-353', 'score': 0.9976177696550971}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-16.html', 'title': 'N-16', 'score': 0.9960355493661447}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-550.html', 'title': 'N-550', 'score': 0.9954471808065942}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-355.html', 'title': 'N-355', 'score': 0.9948149467188039}]
result = search.search('cherry lime cherry apple tomato papaya',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #1 checking search results for 'cherry lime cherry apple tomato papaya' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #1 checking search results for 'cherry lime cherry apple tomato papaya' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #2 checking search results for 'coconut tomato banana banana kiwi orange kiwi' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-540.html', 'title': 'N-540', 'score': 0.999901559603225}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-599.html', 'title': 'N-599', 'score': 0.9998498427810806}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-921.html', 'title': 'N-921', 'score': 0.9982614201978356}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-781.html', 'title': 'N-781', 'score': 0.9980299146750804}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-901.html', 'title': 'N-901', 'score': 0.9979933424318027}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-289.html', 'title': 'N-289', 'score': 0.9976704869269005}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-891.html', 'title': 'N-891', 'score': 0.9974584642947542}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-153.html', 'title': 'N-153', 'score': 0.9960745680589984}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-851.html', 'title': 'N-851', 'score': 0.9958370067047411}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-323.html', 'title': 'N-323', 'score': 0.99580959119611}]
result = search.search('coconut tomato banana banana kiwi orange kiwi',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #2 checking search results for 'coconut tomato banana banana kiwi orange kiwi' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #2 checking search results for 'coconut tomato banana banana kiwi orange kiwi' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #3 checking search results for 'papaya fig fig banana apricot fig cherry' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-953.html', 'title': 'N-953', 'score': 0.9996933021718666}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-74.html', 'title': 'N-74', 'score': 0.9917208278896824}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-918.html', 'title': 'N-918', 'score': 0.9904804162250446}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-534.html', 'title': 'N-534', 'score': 0.9890811831997427}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-262.html', 'title': 'N-262', 'score': 0.9889577121723885}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-689.html', 'title': 'N-689', 'score': 0.9886890166625675}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-475.html', 'title': 'N-475', 'score': 0.9855879631800645}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-462.html', 'title': 'N-462', 'score': 0.9850456617254015}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-674.html', 'title': 'N-674', 'score': 0.9837008557775769}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-566.html', 'title': 'N-566', 'score': 0.9797339873763047}]
result = search.search('papaya fig fig banana apricot fig cherry',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #3 checking search results for 'papaya fig fig banana apricot fig cherry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #3 checking search results for 'papaya fig fig banana apricot fig cherry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #4 checking search results for 'kiwi peach orange papaya coconut papaya lime tomato' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-544.html', 'title': 'N-544', 'score': 0.9952633396221527}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-264.html', 'title': 'N-264', 'score': 0.9932265236125681}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-739.html', 'title': 'N-739', 'score': 0.9897103165980314}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-332.html', 'title': 'N-332', 'score': 0.9895300064766615}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-737.html', 'title': 'N-737', 'score': 0.9894688994832144}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-322.html', 'title': 'N-322', 'score': 0.9894671760218111}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-797.html', 'title': 'N-797', 'score': 0.9886883830955147}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-371.html', 'title': 'N-371', 'score': 0.9876609737214124}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-954.html', 'title': 'N-954', 'score': 0.985477503444637}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-816.html', 'title': 'N-816', 'score': 0.985344775278269}]
result = search.search('kiwi peach orange papaya coconut papaya lime tomato',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #4 checking search results for 'kiwi peach orange papaya coconut papaya lime tomato' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #4 checking search results for 'kiwi peach orange papaya coconut papaya lime tomato' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #5 checking search results for 'apple banana cherry blueberry peach blueberry banana kiwi' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-522.html', 'title': 'N-522', 'score': 0.9918658203617542}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-226.html', 'title': 'N-226', 'score': 0.991060495699012}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-879.html', 'title': 'N-879', 'score': 0.9909327335920476}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-937.html', 'title': 'N-937', 'score': 0.9907385565192556}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-193.html', 'title': 'N-193', 'score': 0.9894480110699017}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-408.html', 'title': 'N-408', 'score': 0.9889859869435261}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-776.html', 'title': 'N-776', 'score': 0.9886234676338929}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-928.html', 'title': 'N-928', 'score': 0.9846689478699999}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-581.html', 'title': 'N-581', 'score': 0.9828155464402392}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-181.html', 'title': 'N-181', 'score': 0.9821309531475781}]
result = search.search('apple banana cherry blueberry peach blueberry banana kiwi',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #5 checking search results for 'apple banana cherry blueberry peach blueberry banana kiwi' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #5 checking search results for 'apple banana cherry blueberry peach blueberry banana kiwi' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #6 checking search results for 'kiwi orange lime fig lime blueberry blueberry' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-78.html', 'title': 'N-78', 'score': 0.9956630342822047}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-277.html', 'title': 'N-277', 'score': 0.993880283982506}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-617.html', 'title': 'N-617', 'score': 0.9934867702294375}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-960.html', 'title': 'N-960', 'score': 0.9918702455214424}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-348.html', 'title': 'N-348', 'score': 0.9916642997601002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-294.html', 'title': 'N-294', 'score': 0.9904506192999564}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-634.html', 'title': 'N-634', 'score': 0.9899327493612818}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-900.html', 'title': 'N-900', 'score': 0.9882774437813865}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-156.html', 'title': 'N-156', 'score': 0.9879362578911062}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-244.html', 'title': 'N-244', 'score': 0.9875399118794518}]
result = search.search('kiwi orange lime fig lime blueberry blueberry',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #6 checking search results for 'kiwi orange lime fig lime blueberry blueberry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #6 checking search results for 'kiwi orange lime fig lime blueberry blueberry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #7 checking search results for 'blueberry orange pear banana papaya' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-756.html', 'title': 'N-756', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-760.html', 'title': 'N-760', 'score': 0.9974956657407102}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-546.html', 'title': 'N-546', 'score': 0.9967956428837992}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-991.html', 'title': 'N-991', 'score': 0.9967625053249078}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-394.html', 'title': 'N-394', 'score': 0.99624854049467}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-824.html', 'title': 'N-824', 'score': 0.9961879528899206}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-484.html', 'title': 'N-484', 'score': 0.9961474975546631}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-210.html', 'title': 'N-210', 'score': 0.9951073443329655}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-667.html', 'title': 'N-667', 'score': 0.9948122003094368}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-675.html', 'title': 'N-675', 'score': 0.9942871502120214}]
result = search.search('blueberry orange pear banana papaya',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #7 checking search results for 'blueberry orange pear banana papaya' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #7 checking search results for 'blueberry orange pear banana papaya' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #8 checking search results for 'blueberry peach blueberry cherry coconut lime tomato orange' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-18.html', 'title': 'N-18', 'score': 0.99997804001549}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-810.html', 'title': 'N-810', 'score': 0.9999110836379508}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-90.html', 'title': 'N-90', 'score': 0.9998921418636046}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-879.html', 'title': 'N-879', 'score': 0.9982567319028895}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-226.html', 'title': 'N-226', 'score': 0.9978915811834234}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-113.html', 'title': 'N-113', 'score': 0.9952184189044292}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-739.html', 'title': 'N-739', 'score': 0.9943758958320611}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-230.html', 'title': 'N-230', 'score': 0.9929107990586999}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-952.html', 'title': 'N-952', 'score': 0.9922678825446586}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-614.html', 'title': 'N-614', 'score': 0.9914914708388509}]
result = search.search('blueberry peach blueberry cherry coconut lime tomato orange',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #8 checking search results for 'blueberry peach blueberry cherry coconut lime tomato orange' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #8 checking search results for 'blueberry peach blueberry cherry coconut lime tomato orange' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #9 checking search results for 'banana blueberry apple pear banana apple apricot cherry' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-852.html', 'title': 'N-852', 'score': 0.996245419174312}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-69.html', 'title': 'N-69', 'score': 0.9955413621164143}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-498.html', 'title': 'N-498', 'score': 0.9927760006548311}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-174.html', 'title': 'N-174', 'score': 0.9903070783797916}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-697.html', 'title': 'N-697', 'score': 0.9894348543608784}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-115.html', 'title': 'N-115', 'score': 0.9878841586793458}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-43.html', 'title': 'N-43', 'score': 0.9877105949236806}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-211.html', 'title': 'N-211', 'score': 0.9870038373907819}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-766.html', 'title': 'N-766', 'score': 0.9868351227713491}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-87.html', 'title': 'N-87', 'score': 0.9862140729617777}]
result = search.search('banana blueberry apple pear banana apple apricot cherry',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #9 checking search results for 'banana blueberry apple pear banana apple apricot cherry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #9 checking search results for 'banana blueberry apple pear banana apple apricot cherry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #10 checking search results for 'blueberry tomato kiwi banana lime kiwi' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-967.html', 'title': 'N-967', 'score': 0.9998185787882649}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-8.html', 'title': 'N-8', 'score': 0.9997567472518738}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-96.html', 'title': 'N-96', 'score': 0.999743909100642}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-191.html', 'title': 'N-191', 'score': 0.999743909100642}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-202.html', 'title': 'N-202', 'score': 0.9997103169095226}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-659.html', 'title': 'N-659', 'score': 0.9996596721399271}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-257.html', 'title': 'N-257', 'score': 0.9983285808503436}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-872.html', 'title': 'N-872', 'score': 0.9979277489553422}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-427.html', 'title': 'N-427', 'score': 0.9979207693971351}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-919.html', 'title': 'N-919', 'score': 0.9961236103693255}]
result = search.search('blueberry tomato kiwi banana lime kiwi',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #10 checking search results for 'blueberry tomato kiwi banana lime kiwi' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #10 checking search results for 'blueberry tomato kiwi banana lime kiwi' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #11 checking search results for 'banana papaya kiwi coconut apricot blueberry orange kiwi' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-927.html', 'title': 'N-927', 'score': 0.9926421665852649}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-675.html', 'title': 'N-675', 'score': 0.9901833627757487}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-235.html', 'title': 'N-235', 'score': 0.9897095560230219}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-919.html', 'title': 'N-919', 'score': 0.9881054750627305}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-542.html', 'title': 'N-542', 'score': 0.9880304357768184}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-427.html', 'title': 'N-427', 'score': 0.9876563986498552}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-300.html', 'title': 'N-300', 'score': 0.9872748242365712}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-692.html', 'title': 'N-692', 'score': 0.9864707792036195}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-697.html', 'title': 'N-697', 'score': 0.9858618559858605}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-814.html', 'title': 'N-814', 'score': 0.9850170658279856}]
result = search.search('banana papaya kiwi coconut apricot blueberry orange kiwi',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #11 checking search results for 'banana papaya kiwi coconut apricot blueberry orange kiwi' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #11 checking search results for 'banana papaya kiwi coconut apricot blueberry orange kiwi' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #12 checking search results for 'cherry banana fig lime tomato blueberry tomato' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-8.html', 'title': 'N-8', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-394.html', 'title': 'N-394', 'score': 0.9973198572478222}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-555.html', 'title': 'N-555', 'score': 0.9963817726596883}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-448.html', 'title': 'N-448', 'score': 0.996284582982601}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-610.html', 'title': 'N-610', 'score': 0.9959932599380938}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-824.html', 'title': 'N-824', 'score': 0.9949624441799957}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-286.html', 'title': 'N-286', 'score': 0.9948126503408999}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-968.html', 'title': 'N-968', 'score': 0.9948118908060839}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-722.html', 'title': 'N-722', 'score': 0.9946628399595526}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-539.html', 'title': 'N-539', 'score': 0.9943976570519147}]
result = search.search('cherry banana fig lime tomato blueberry tomato',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #12 checking search results for 'cherry banana fig lime tomato blueberry tomato' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #12 checking search results for 'cherry banana fig lime tomato blueberry tomato' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #13 checking search results for 'fig coconut apricot cherry banana coconut pear blueberry' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-887.html', 'title': 'N-887', 'score': 0.9933924978192819}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-448.html', 'title': 'N-448', 'score': 0.9906984429730852}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-384.html', 'title': 'N-384', 'score': 0.9902767069215553}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-964.html', 'title': 'N-964', 'score': 0.9893643514074139}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-765.html', 'title': 'N-765', 'score': 0.9893626742464464}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-695.html', 'title': 'N-695', 'score': 0.987157902345618}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-76.html', 'title': 'N-76', 'score': 0.9870435234197827}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-192.html', 'title': 'N-192', 'score': 0.9864365077188278}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-555.html', 'title': 'N-555', 'score': 0.9842871315203338}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-991.html', 'title': 'N-991', 'score': 0.9842030314521159}]
result = search.search('fig coconut apricot cherry banana coconut pear blueberry',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #13 checking search results for 'fig coconut apricot cherry banana coconut pear blueberry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #13 checking search results for 'fig coconut apricot cherry banana coconut pear blueberry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #14 checking search results for 'fig tomato kiwi kiwi coconut apricot lime fig' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-411.html', 'title': 'N-411', 'score': 0.9969220614673054}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-590.html', 'title': 'N-590', 'score': 0.9962389377419617}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-195.html', 'title': 'N-195', 'score': 0.9932074165522182}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-147.html', 'title': 'N-147', 'score': 0.9931509139842348}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-952.html', 'title': 'N-952', 'score': 0.9930502351182873}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-427.html', 'title': 'N-427', 'score': 0.9929846941869577}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-758.html', 'title': 'N-758', 'score': 0.9928381990787161}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-174.html', 'title': 'N-174', 'score': 0.9927336218101721}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-331.html', 'title': 'N-331', 'score': 0.99099562011354}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-461.html', 'title': 'N-461', 'score': 0.9898953023901658}]
result = search.search('fig tomato kiwi kiwi coconut apricot lime fig',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #14 checking search results for 'fig tomato kiwi kiwi coconut apricot lime fig' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #14 checking search results for 'fig tomato kiwi kiwi coconut apricot lime fig' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #15 checking search results for 'coconut kiwi pear blueberry orange pear apple' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-678.html', 'title': 'N-678', 'score': 0.9961976073763279}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-204.html', 'title': 'N-204', 'score': 0.9932900330464063}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-938.html', 'title': 'N-938', 'score': 0.9859974001034965}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-85.html', 'title': 'N-85', 'score': 0.9857402923348131}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-681.html', 'title': 'N-681', 'score': 0.9848658792747838}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-435.html', 'title': 'N-435', 'score': 0.9845864778934915}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-619.html', 'title': 'N-619', 'score': 0.9833592142633594}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-523.html', 'title': 'N-523', 'score': 0.9833206045912756}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-321.html', 'title': 'N-321', 'score': 0.9829635027122982}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-93.html', 'title': 'N-93', 'score': 0.9828346446581492}]
result = search.search('coconut kiwi pear blueberry orange pear apple',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #15 checking search results for 'coconut kiwi pear blueberry orange pear apple' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #15 checking search results for 'coconut kiwi pear blueberry orange pear apple' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #16 checking search results for 'pear cherry cherry orange orange papaya orange' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-845.html', 'title': 'N-845', 'score': 0.9980085519833581}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-801.html', 'title': 'N-801', 'score': 0.995680752035392}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-148.html', 'title': 'N-148', 'score': 0.9938120139872244}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-238.html', 'title': 'N-238', 'score': 0.9929609084901575}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-380.html', 'title': 'N-380', 'score': 0.9922653708802158}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-446.html', 'title': 'N-446', 'score': 0.9907155937667803}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-57.html', 'title': 'N-57', 'score': 0.9906963755730961}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-682.html', 'title': 'N-682', 'score': 0.9891758337966392}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-951.html', 'title': 'N-951', 'score': 0.9882987507591838}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-248.html', 'title': 'N-248', 'score': 0.9871409833439103}]
result = search.search('pear cherry cherry orange orange papaya orange',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #16 checking search results for 'pear cherry cherry orange orange papaya orange' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #16 checking search results for 'pear cherry cherry orange orange papaya orange' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #17 checking search results for 'papaya blueberry blueberry papaya tomato lime banana coconut' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-413.html', 'title': 'N-413', 'score': 0.99992928388755}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-439.html', 'title': 'N-439', 'score': 0.9972677178263312}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-673.html', 'title': 'N-673', 'score': 0.9948588376865887}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-1.html', 'title': 'N-1', 'score': 0.9937881518338582}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-739.html', 'title': 'N-739', 'score': 0.9933849290222639}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-894.html', 'title': 'N-894', 'score': 0.9933514041018369}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-441.html', 'title': 'N-441', 'score': 0.9930216273879707}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-322.html', 'title': 'N-322', 'score': 0.9915459557721549}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-230.html', 'title': 'N-230', 'score': 0.9910467277600473}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-445.html', 'title': 'N-445', 'score': 0.9903137131297114}]
result = search.search('papaya blueberry blueberry papaya tomato lime banana coconut',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #17 checking search results for 'papaya blueberry blueberry papaya tomato lime banana coconut' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #17 checking search results for 'papaya blueberry blueberry papaya tomato lime banana coconut' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #18 checking search results for 'fig kiwi apricot orange kiwi' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-971.html', 'title': 'N-971', 'score': 0.9996348912414244}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-866.html', 'title': 'N-866', 'score': 0.9995726243080898}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-754.html', 'title': 'N-754', 'score': 0.9995535541956646}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-867.html', 'title': 'N-867', 'score': 0.9995418774228123}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-91.html', 'title': 'N-91', 'score': 0.9995363211552685}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-370.html', 'title': 'N-370', 'score': 0.9993265128495961}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-927.html', 'title': 'N-927', 'score': 0.9983289472184101}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-259.html', 'title': 'N-259', 'score': 0.9982606092316005}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-198.html', 'title': 'N-198', 'score': 0.9978188766132883}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-355.html', 'title': 'N-355', 'score': 0.9977890952204238}]
result = search.search('fig kiwi apricot orange kiwi',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #18 checking search results for 'fig kiwi apricot orange kiwi' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #18 checking search results for 'fig kiwi apricot orange kiwi' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #19 checking search results for 'pear cherry coconut lime pear cherry apricot' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-22.html', 'title': 'N-22', 'score': 0.9998640158415655}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-684.html', 'title': 'N-684', 'score': 0.9998468866051712}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-342.html', 'title': 'N-342', 'score': 0.9952731388702813}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-257.html', 'title': 'N-257', 'score': 0.9929775731635826}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-731.html', 'title': 'N-731', 'score': 0.9926033808934669}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-411.html', 'title': 'N-411', 'score': 0.9920114987229358}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-775.html', 'title': 'N-775', 'score': 0.9918119686444656}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-427.html', 'title': 'N-427', 'score': 0.9907909615517793}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-986.html', 'title': 'N-986', 'score': 0.9897202265811023}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-752.html', 'title': 'N-752', 'score': 0.9893312967005532}]
result = search.search('pear cherry coconut lime pear cherry apricot',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #19 checking search results for 'pear cherry coconut lime pear cherry apricot' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #19 checking search results for 'pear cherry coconut lime pear cherry apricot' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #20 checking search results for 'banana lime coconut blueberry banana coconut blueberry' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-805.html', 'title': 'N-805', 'score': 0.999940094732585}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-720.html', 'title': 'N-720', 'score': 0.9999353962986607}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-892.html', 'title': 'N-892', 'score': 0.9999071666898914}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-266.html', 'title': 'N-266', 'score': 0.9978584111398979}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-430.html', 'title': 'N-430', 'score': 0.9973574320474489}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-637.html', 'title': 'N-637', 'score': 0.9966108611259894}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-370.html', 'title': 'N-370', 'score': 0.9965949289034927}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-482.html', 'title': 'N-482', 'score': 0.9962802309531102}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-478.html', 'title': 'N-478', 'score': 0.9961782028576396}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-210.html', 'title': 'N-210', 'score': 0.996105601723548}]
result = search.search('banana lime coconut blueberry banana coconut blueberry',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #20 checking search results for 'banana lime coconut blueberry banana coconut blueberry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #20 checking search results for 'banana lime coconut blueberry banana coconut blueberry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #21 checking search results for 'kiwi tomato tomato kiwi blueberry apple kiwi kiwi' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-665.html', 'title': 'N-665', 'score': 0.9996640523754927}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-203.html', 'title': 'N-203', 'score': 0.9995113317211473}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-799.html', 'title': 'N-799', 'score': 0.9994832558414424}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-118.html', 'title': 'N-118', 'score': 0.999449120127785}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-433.html', 'title': 'N-433', 'score': 0.9981913629571606}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-565.html', 'title': 'N-565', 'score': 0.9980983670346818}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-980.html', 'title': 'N-980', 'score': 0.9977349391908008}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-611.html', 'title': 'N-611', 'score': 0.9977036445829603}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-116.html', 'title': 'N-116', 'score': 0.9973132445521573}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-750.html', 'title': 'N-750', 'score': 0.9962861707376685}]
result = search.search('kiwi tomato tomato kiwi blueberry apple kiwi kiwi',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #21 checking search results for 'kiwi tomato tomato kiwi blueberry apple kiwi kiwi' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #21 checking search results for 'kiwi tomato tomato kiwi blueberry apple kiwi kiwi' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #22 checking search results for 'banana lime orange coconut apricot banana lime orange' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-644.html', 'title': 'N-644', 'score': 0.998415778477506}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-860.html', 'title': 'N-860', 'score': 0.9951205916249467}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-241.html', 'title': 'N-241', 'score': 0.9938366323051052}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-80.html', 'title': 'N-80', 'score': 0.9937844647304082}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-383.html', 'title': 'N-383', 'score': 0.9932224033697364}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-731.html', 'title': 'N-731', 'score': 0.992998337523173}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-986.html', 'title': 'N-986', 'score': 0.9929651890710453}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-750.html', 'title': 'N-750', 'score': 0.9927650369463438}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-388.html', 'title': 'N-388', 'score': 0.9924955788756381}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-517.html', 'title': 'N-517', 'score': 0.9920987064611791}]
result = search.search('banana lime orange coconut apricot banana lime orange',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #22 checking search results for 'banana lime orange coconut apricot banana lime orange' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #22 checking search results for 'banana lime orange coconut apricot banana lime orange' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #23 checking search results for 'apple fig lime pear orange pear banana' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-678.html', 'title': 'N-678', 'score': 0.9962122582467352}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-378.html', 'title': 'N-378', 'score': 0.9928670858620481}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-160.html', 'title': 'N-160', 'score': 0.9928133625892911}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-84.html', 'title': 'N-84', 'score': 0.986516946639167}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-496.html', 'title': 'N-496', 'score': 0.9862947727460585}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-712.html', 'title': 'N-712', 'score': 0.9857369025943871}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-230.html', 'title': 'N-230', 'score': 0.9853484254943209}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-950.html', 'title': 'N-950', 'score': 0.9853040490550504}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-385.html', 'title': 'N-385', 'score': 0.9845339152135788}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-76.html', 'title': 'N-76', 'score': 0.9838966022759871}]
result = search.search('apple fig lime pear orange pear banana',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #23 checking search results for 'apple fig lime pear orange pear banana' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #23 checking search results for 'apple fig lime pear orange pear banana' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #24 checking search results for 'cherry cherry fig banana orange cherry cherry' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-867.html', 'title': 'N-867', 'score': 0.9989989154464439}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-862.html', 'title': 'N-862', 'score': 0.9977784120148723}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-275.html', 'title': 'N-275', 'score': 0.9975329301341344}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-173.html', 'title': 'N-173', 'score': 0.9965668023577001}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-619.html', 'title': 'N-619', 'score': 0.993846578594255}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-342.html', 'title': 'N-342', 'score': 0.9919386199357946}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-120.html', 'title': 'N-120', 'score': 0.9880843077360943}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-920.html', 'title': 'N-920', 'score': 0.9880618621977157}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-378.html', 'title': 'N-378', 'score': 0.9876400531837161}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-417.html', 'title': 'N-417', 'score': 0.9875440892355346}]
result = search.search('cherry cherry fig banana orange cherry cherry',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #24 checking search results for 'cherry cherry fig banana orange cherry cherry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #24 checking search results for 'cherry cherry fig banana orange cherry cherry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #25 checking search results for 'coconut apricot orange fig fig orange' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-533.html', 'title': 'N-533', 'score': 0.9993253154678023}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-986.html', 'title': 'N-986', 'score': 0.9970051211952535}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-731.html', 'title': 'N-731', 'score': 0.9963463280755379}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-860.html', 'title': 'N-860', 'score': 0.9958003637743811}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-817.html', 'title': 'N-817', 'score': 0.9957752645118282}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-402.html', 'title': 'N-402', 'score': 0.9956420395142284}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-302.html', 'title': 'N-302', 'score': 0.9953581369479015}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-990.html', 'title': 'N-990', 'score': 0.9945972405075685}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-332.html', 'title': 'N-332', 'score': 0.9942751961959735}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-465.html', 'title': 'N-465', 'score': 0.9942199764413359}]
result = search.search('coconut apricot orange fig fig orange',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #25 checking search results for 'coconut apricot orange fig fig orange' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #25 checking search results for 'coconut apricot orange fig fig orange' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #26 checking search results for 'apricot kiwi apple orange peach lime orange' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-94.html', 'title': 'N-94', 'score': 0.9970314325806091}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-704.html', 'title': 'N-704', 'score': 0.993637234545726}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-889.html', 'title': 'N-889', 'score': 0.9923886635681543}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-677.html', 'title': 'N-677', 'score': 0.992212621178322}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-976.html', 'title': 'N-976', 'score': 0.9910432235196228}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-234.html', 'title': 'N-234', 'score': 0.9892617326555041}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-408.html', 'title': 'N-408', 'score': 0.9884757907306031}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-71.html', 'title': 'N-71', 'score': 0.9874623945838307}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-963.html', 'title': 'N-963', 'score': 0.9841417074056098}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-164.html', 'title': 'N-164', 'score': 0.9833670022772066}]
result = search.search('apricot kiwi apple orange peach lime orange',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #26 checking search results for 'apricot kiwi apple orange peach lime orange' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #26 checking search results for 'apricot kiwi apple orange peach lime orange' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #27 checking search results for 'peach banana orange peach cherry coconut papaya' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-254.html', 'title': 'N-254', 'score': 0.9974058041404142}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-864.html', 'title': 'N-864', 'score': 0.9938157342800531}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-576.html', 'title': 'N-576', 'score': 0.990914450392737}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-465.html', 'title': 'N-465', 'score': 0.9871266737937048}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-606.html', 'title': 'N-606', 'score': 0.9861089799920872}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-914.html', 'title': 'N-914', 'score': 0.9853995762730203}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-141.html', 'title': 'N-141', 'score': 0.9842846635444862}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-80.html', 'title': 'N-80', 'score': 0.984263543675635}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-156.html', 'title': 'N-156', 'score': 0.9842435290020328}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-614.html', 'title': 'N-614', 'score': 0.9832404333573307}]
result = search.search('peach banana orange peach cherry coconut papaya',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #27 checking search results for 'peach banana orange peach cherry coconut papaya' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #27 checking search results for 'peach banana orange peach cherry coconut papaya' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #28 checking search results for 'cherry peach blueberry pear orange kiwi blueberry lime' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-226.html', 'title': 'N-226', 'score': 0.9980464436541072}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-879.html', 'title': 'N-879', 'score': 0.9912560079971644}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-739.html', 'title': 'N-739', 'score': 0.9912267109890953}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-322.html', 'title': 'N-322', 'score': 0.988872074067766}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-464.html', 'title': 'N-464', 'score': 0.9885875421407365}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-336.html', 'title': 'N-336', 'score': 0.9883175366489922}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-952.html', 'title': 'N-952', 'score': 0.9845846412448378}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-262.html', 'title': 'N-262', 'score': 0.9834762288027233}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-522.html', 'title': 'N-522', 'score': 0.9828261910839344}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-255.html', 'title': 'N-255', 'score': 0.9819081189122975}]
result = search.search('cherry peach blueberry pear orange kiwi blueberry lime',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #28 checking search results for 'cherry peach blueberry pear orange kiwi blueberry lime' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #28 checking search results for 'cherry peach blueberry pear orange kiwi blueberry lime' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #29 checking search results for 'tomato kiwi kiwi apricot pear coconut' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-768.html', 'title': 'N-768', 'score': 0.9998783195885601}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-562.html', 'title': 'N-562', 'score': 0.9998184200504407}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-372.html', 'title': 'N-372', 'score': 0.9960476983739277}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-203.html', 'title': 'N-203', 'score': 0.9960302359069855}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-927.html', 'title': 'N-927', 'score': 0.994805497804238}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-420.html', 'title': 'N-420', 'score': 0.9940847669287246}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-121.html', 'title': 'N-121', 'score': 0.9933331301914153}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-45.html', 'title': 'N-45', 'score': 0.9931089569290003}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-899.html', 'title': 'N-899', 'score': 0.9931020327751069}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-235.html', 'title': 'N-235', 'score': 0.9927292134559399}]
result = search.search('tomato kiwi kiwi apricot pear coconut',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #29 checking search results for 'tomato kiwi kiwi apricot pear coconut' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #29 checking search results for 'tomato kiwi kiwi apricot pear coconut' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #30 checking search results for 'blueberry cherry papaya cherry apple kiwi peach cherry' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-553.html', 'title': 'N-553', 'score': 0.9998448289019746}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-619.html', 'title': 'N-619', 'score': 0.9944605293790858}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-187.html', 'title': 'N-187', 'score': 0.9928402039524594}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-752.html', 'title': 'N-752', 'score': 0.9802688156988897}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-716.html', 'title': 'N-716', 'score': 0.979117171639871}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-235.html', 'title': 'N-235', 'score': 0.9738452109264953}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-896.html', 'title': 'N-896', 'score': 0.9734044880901045}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-407.html', 'title': 'N-407', 'score': 0.9732819866635634}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-492.html', 'title': 'N-492', 'score': 0.9729595028328232}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-583.html', 'title': 'N-583', 'score': 0.9714311730742522}]
result = search.search('blueberry cherry papaya cherry apple kiwi peach cherry',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #30 checking search results for 'blueberry cherry papaya cherry apple kiwi peach cherry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #30 checking search results for 'blueberry cherry papaya cherry apple kiwi peach cherry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #31 checking search results for 'kiwi pear lime kiwi blueberry' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-26.html', 'title': 'N-26', 'score': 0.9996965444830187}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-562.html', 'title': 'N-562', 'score': 0.9996965444830187}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-8.html', 'title': 'N-8', 'score': 0.9996177891161696}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-666.html', 'title': 'N-666', 'score': 0.9984073159710771}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-566.html', 'title': 'N-566', 'score': 0.9978777767728522}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-872.html', 'title': 'N-872', 'score': 0.9968036570390364}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-174.html', 'title': 'N-174', 'score': 0.9964846357788664}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-43.html', 'title': 'N-43', 'score': 0.9964782184256283}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-919.html', 'title': 'N-919', 'score': 0.9952475829024086}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-188.html', 'title': 'N-188', 'score': 0.9951078390436426}]
result = search.search('kiwi pear lime kiwi blueberry',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #31 checking search results for 'kiwi pear lime kiwi blueberry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #31 checking search results for 'kiwi pear lime kiwi blueberry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #32 checking search results for 'papaya fig tomato kiwi peach peach' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-220.html', 'title': 'N-220', 'score': 0.99978992421379}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-908.html', 'title': 'N-908', 'score': 0.9997668361330997}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-560.html', 'title': 'N-560', 'score': 0.9997527919100798}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-893.html', 'title': 'N-893', 'score': 0.9984490185682406}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-568.html', 'title': 'N-568', 'score': 0.9977847658979256}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-448.html', 'title': 'N-448', 'score': 0.9975381403091265}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-622.html', 'title': 'N-622', 'score': 0.9975340042336933}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-211.html', 'title': 'N-211', 'score': 0.9962322172015515}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-465.html', 'title': 'N-465', 'score': 0.9960005197475658}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-505.html', 'title': 'N-505', 'score': 0.9954603264243505}]
result = search.search('papaya fig tomato kiwi peach peach',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #32 checking search results for 'papaya fig tomato kiwi peach peach' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #32 checking search results for 'papaya fig tomato kiwi peach peach' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #33 checking search results for 'apple fig papaya kiwi peach apple blueberry apricot' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-582.html', 'title': 'N-582', 'score': 0.9904905916363651}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-590.html', 'title': 'N-590', 'score': 0.987771620251096}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-765.html', 'title': 'N-765', 'score': 0.9869183070728343}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-429.html', 'title': 'N-429', 'score': 0.9850725249057009}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-440.html', 'title': 'N-440', 'score': 0.9840566461597361}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-907.html', 'title': 'N-907', 'score': 0.9825717130351733}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-50.html', 'title': 'N-50', 'score': 0.9810230034039008}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-643.html', 'title': 'N-643', 'score': 0.9805932684470339}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-395.html', 'title': 'N-395', 'score': 0.9805365713998069}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-628.html', 'title': 'N-628', 'score': 0.9803031860930146}]
result = search.search('apple fig papaya kiwi peach apple blueberry apricot',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #33 checking search results for 'apple fig papaya kiwi peach apple blueberry apricot' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #33 checking search results for 'apple fig papaya kiwi peach apple blueberry apricot' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #34 checking search results for 'coconut orange apricot apple tomato orange pear banana' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-71.html', 'title': 'N-71', 'score': 0.9948385424346818}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-208.html', 'title': 'N-208', 'score': 0.9947992287587663}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-762.html', 'title': 'N-762', 'score': 0.9929705041585339}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-963.html', 'title': 'N-963', 'score': 0.9917954741285817}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-525.html', 'title': 'N-525', 'score': 0.9913614709001503}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-234.html', 'title': 'N-234', 'score': 0.9891844559979898}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-751.html', 'title': 'N-751', 'score': 0.9888666640566358}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-148.html', 'title': 'N-148', 'score': 0.9888621242249489}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-258.html', 'title': 'N-258', 'score': 0.9874047840281633}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-94.html', 'title': 'N-94', 'score': 0.9869792030919363}]
result = search.search('coconut orange apricot apple tomato orange pear banana',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #34 checking search results for 'coconut orange apricot apple tomato orange pear banana' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #34 checking search results for 'coconut orange apricot apple tomato orange pear banana' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #35 checking search results for 'banana banana apple fig lime coconut kiwi' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-390.html', 'title': 'N-390', 'score': 0.9998642873005815}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-937.html', 'title': 'N-937', 'score': 0.9930577616452256}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-526.html', 'title': 'N-526', 'score': 0.9928825219885702}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-704.html', 'title': 'N-704', 'score': 0.9903263649851142}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-94.html', 'title': 'N-94', 'score': 0.9897170742179612}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-226.html', 'title': 'N-226', 'score': 0.9894405182841659}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-42.html', 'title': 'N-42', 'score': 0.9885093025466491}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-834.html', 'title': 'N-834', 'score': 0.9880012369857047}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-248.html', 'title': 'N-248', 'score': 0.9875922042940192}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-966.html', 'title': 'N-966', 'score': 0.9875197034710455}]
result = search.search('banana banana apple fig lime coconut kiwi',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #35 checking search results for 'banana banana apple fig lime coconut kiwi' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #35 checking search results for 'banana banana apple fig lime coconut kiwi' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #36 checking search results for 'orange apricot lime banana apricot cherry kiwi' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-810.html', 'title': 'N-810', 'score': 0.9998624137041852}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-296.html', 'title': 'N-296', 'score': 0.992920673687098}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-623.html', 'title': 'N-623', 'score': 0.9899187659922946}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-680.html', 'title': 'N-680', 'score': 0.9897681435007174}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-11.html', 'title': 'N-11', 'score': 0.9894936319789561}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-617.html', 'title': 'N-617', 'score': 0.9881803310591122}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-844.html', 'title': 'N-844', 'score': 0.9854757263049453}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-176.html', 'title': 'N-176', 'score': 0.9853947980324913}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-651.html', 'title': 'N-651', 'score': 0.9849941804599536}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-210.html', 'title': 'N-210', 'score': 0.983061603238473}]
result = search.search('orange apricot lime banana apricot cherry kiwi',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #36 checking search results for 'orange apricot lime banana apricot cherry kiwi' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #36 checking search results for 'orange apricot lime banana apricot cherry kiwi' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #37 checking search results for 'apple blueberry fig lime peach fig' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-123.html', 'title': 'N-123', 'score': 0.9998765442687622}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-978.html', 'title': 'N-978', 'score': 0.999834476953073}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-200.html', 'title': 'N-200', 'score': 0.9997980079190885}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-684.html', 'title': 'N-684', 'score': 0.999727134465411}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-55.html', 'title': 'N-55', 'score': 0.99510979495959}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-391.html', 'title': 'N-391', 'score': 0.9949983667007603}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-427.html', 'title': 'N-427', 'score': 0.9911749786167606}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-903.html', 'title': 'N-903', 'score': 0.990239336208714}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-245.html', 'title': 'N-245', 'score': 0.989811837071373}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-637.html', 'title': 'N-637', 'score': 0.9896114053766496}]
result = search.search('apple blueberry fig lime peach fig',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #37 checking search results for 'apple blueberry fig lime peach fig' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #37 checking search results for 'apple blueberry fig lime peach fig' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #38 checking search results for 'apricot coconut apricot apple kiwi orange tomato' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-103.html', 'title': 'N-103', 'score': 0.9999945504788582}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-810.html', 'title': 'N-810', 'score': 0.9998608696100253}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-680.html', 'title': 'N-680', 'score': 0.9979942161967472}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-314.html', 'title': 'N-314', 'score': 0.9946798774165452}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-296.html', 'title': 'N-296', 'score': 0.99347109891977}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-86.html', 'title': 'N-86', 'score': 0.9928465994913038}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-106.html', 'title': 'N-106', 'score': 0.9923604124969446}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-334.html', 'title': 'N-334', 'score': 0.9913169317729635}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-623.html', 'title': 'N-623', 'score': 0.9905624799305862}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-873.html', 'title': 'N-873', 'score': 0.9905382419617872}]
result = search.search('apricot coconut apricot apple kiwi orange tomato',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #38 checking search results for 'apricot coconut apricot apple kiwi orange tomato' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #38 checking search results for 'apricot coconut apricot apple kiwi orange tomato' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #39 checking search results for 'kiwi coconut blueberry apple coconut kiwi cherry banana' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-8.html', 'title': 'N-8', 'score': 0.9999026891310655}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-709.html', 'title': 'N-709', 'score': 0.993788989098407}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-630.html', 'title': 'N-630', 'score': 0.9937162554004665}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-612.html', 'title': 'N-612', 'score': 0.9930685550133561}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-385.html', 'title': 'N-385', 'score': 0.9917409324723652}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-600.html', 'title': 'N-600', 'score': 0.991168383448411}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-341.html', 'title': 'N-341', 'score': 0.9902072521317324}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-611.html', 'title': 'N-611', 'score': 0.9880119366248398}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-598.html', 'title': 'N-598', 'score': 0.987751595606106}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-299.html', 'title': 'N-299', 'score': 0.9873583933768894}]
result = search.search('kiwi coconut blueberry apple coconut kiwi cherry banana',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #39 checking search results for 'kiwi coconut blueberry apple coconut kiwi cherry banana' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #39 checking search results for 'kiwi coconut blueberry apple coconut kiwi cherry banana' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #40 checking search results for 'fig kiwi blueberry orange orange peach apricot coconut' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-94.html', 'title': 'N-94', 'score': 0.9968787757769508}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-704.html', 'title': 'N-704', 'score': 0.9948747249935455}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-963.html', 'title': 'N-963', 'score': 0.9923687713587749}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-429.html', 'title': 'N-429', 'score': 0.990586285127127}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-525.html', 'title': 'N-525', 'score': 0.98727488519875}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-32.html', 'title': 'N-32', 'score': 0.9854322232002093}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-621.html', 'title': 'N-621', 'score': 0.9827654171465307}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-917.html', 'title': 'N-917', 'score': 0.9816860430462749}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-767.html', 'title': 'N-767', 'score': 0.9812940424474935}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-644.html', 'title': 'N-644', 'score': 0.9803956985093005}]
result = search.search('fig kiwi blueberry orange orange peach apricot coconut',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #40 checking search results for 'fig kiwi blueberry orange orange peach apricot coconut' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #40 checking search results for 'fig kiwi blueberry orange orange peach apricot coconut' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #41 checking search results for 'blueberry fig kiwi cherry apple tomato lime lime' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-717.html', 'title': 'N-717', 'score': 0.9969909774080749}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-321.html', 'title': 'N-321', 'score': 0.9930367429070107}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-830.html', 'title': 'N-830', 'score': 0.992688730737895}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-293.html', 'title': 'N-293', 'score': 0.9912589705964386}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-900.html', 'title': 'N-900', 'score': 0.9903684609376818}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-57.html', 'title': 'N-57', 'score': 0.9899281842566412}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-984.html', 'title': 'N-984', 'score': 0.9896518293554624}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-158.html', 'title': 'N-158', 'score': 0.9895150508547359}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-335.html', 'title': 'N-335', 'score': 0.9894611033057015}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-485.html', 'title': 'N-485', 'score': 0.9873431056052427}]
result = search.search('blueberry fig kiwi cherry apple tomato lime lime',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #41 checking search results for 'blueberry fig kiwi cherry apple tomato lime lime' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #41 checking search results for 'blueberry fig kiwi cherry apple tomato lime lime' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #42 checking search results for 'banana lime cherry banana banana tomato peach' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-27.html', 'title': 'N-27', 'score': 0.9998246937397934}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-978.html', 'title': 'N-978', 'score': 0.9997273548462066}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-200.html', 'title': 'N-200', 'score': 0.9996473163578576}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-91.html', 'title': 'N-91', 'score': 0.9993886200608965}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-433.html', 'title': 'N-433', 'score': 0.9987241996741636}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-526.html', 'title': 'N-526', 'score': 0.9986347659009196}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-336.html', 'title': 'N-336', 'score': 0.9976573906606526}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-778.html', 'title': 'N-778', 'score': 0.9974263253555187}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-104.html', 'title': 'N-104', 'score': 0.9957086503684943}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-681.html', 'title': 'N-681', 'score': 0.9935092867535622}]
result = search.search('banana lime cherry banana banana tomato peach',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #42 checking search results for 'banana lime cherry banana banana tomato peach' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #42 checking search results for 'banana lime cherry banana banana tomato peach' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #43 checking search results for 'lime tomato pear coconut banana apple kiwi peach' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-234.html', 'title': 'N-234', 'score': 0.9983360263447955}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-544.html', 'title': 'N-544', 'score': 0.9955944126735535}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-320.html', 'title': 'N-320', 'score': 0.9934301991340083}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-322.html', 'title': 'N-322', 'score': 0.9929370422821489}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-760.html', 'title': 'N-760', 'score': 0.9925315528956731}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-164.html', 'title': 'N-164', 'score': 0.9922461011684088}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-617.html', 'title': 'N-617', 'score': 0.9921985690394987}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-105.html', 'title': 'N-105', 'score': 0.9907049513819627}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-245.html', 'title': 'N-245', 'score': 0.9904138122555669}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-577.html', 'title': 'N-577', 'score': 0.9896866721115412}]
result = search.search('lime tomato pear coconut banana apple kiwi peach',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #43 checking search results for 'lime tomato pear coconut banana apple kiwi peach' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #43 checking search results for 'lime tomato pear coconut banana apple kiwi peach' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #44 checking search results for 'banana lime orange coconut cherry papaya cherry' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-161.html', 'title': 'N-161', 'score': 0.9998489890331963}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-182.html', 'title': 'N-182', 'score': 0.9998145965264408}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-64.html', 'title': 'N-64', 'score': 0.9898625526993222}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-168.html', 'title': 'N-168', 'score': 0.9887132157858922}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-656.html', 'title': 'N-656', 'score': 0.9884659624604807}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-550.html', 'title': 'N-550', 'score': 0.9878845097195736}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-407.html', 'title': 'N-407', 'score': 0.9876984620776343}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-79.html', 'title': 'N-79', 'score': 0.9861422653059799}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-848.html', 'title': 'N-848', 'score': 0.9859892414559798}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-288.html', 'title': 'N-288', 'score': 0.9857057000765348}]
result = search.search('banana lime orange coconut cherry papaya cherry',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #44 checking search results for 'banana lime orange coconut cherry papaya cherry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #44 checking search results for 'banana lime orange coconut cherry papaya cherry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #45 checking search results for 'banana coconut fig kiwi papaya cherry' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-450.html', 'title': 'N-450', 'score': 0.9974331239379338}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-798.html', 'title': 'N-798', 'score': 0.9969834083567742}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-25.html', 'title': 'N-25', 'score': 0.9944012738983629}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-760.html', 'title': 'N-760', 'score': 0.9943837929674849}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-824.html', 'title': 'N-824', 'score': 0.9939446354839803}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-296.html', 'title': 'N-296', 'score': 0.9931744451374639}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-321.html', 'title': 'N-321', 'score': 0.9924857627422142}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-369.html', 'title': 'N-369', 'score': 0.9921831227691474}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-536.html', 'title': 'N-536', 'score': 0.9920181344819967}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-254.html', 'title': 'N-254', 'score': 0.9918469381083036}]
result = search.search('banana coconut fig kiwi papaya cherry',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #45 checking search results for 'banana coconut fig kiwi papaya cherry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #45 checking search results for 'banana coconut fig kiwi papaya cherry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #46 checking search results for 'pear kiwi banana pear cherry papaya tomato tomato' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-128.html', 'title': 'N-128', 'score': 0.9964730817895403}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-536.html', 'title': 'N-536', 'score': 0.9961991366499771}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-576.html', 'title': 'N-576', 'score': 0.9944318575382765}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-454.html', 'title': 'N-454', 'score': 0.9942820338304157}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-110.html', 'title': 'N-110', 'score': 0.9930421605970452}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-12.html', 'title': 'N-12', 'score': 0.9930396272517377}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-176.html', 'title': 'N-176', 'score': 0.9930012096441704}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-917.html', 'title': 'N-917', 'score': 0.9928991152132065}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-724.html', 'title': 'N-724', 'score': 0.9925908595585261}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-178.html', 'title': 'N-178', 'score': 0.9911915988974787}]
result = search.search('pear kiwi banana pear cherry papaya tomato tomato',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #46 checking search results for 'pear kiwi banana pear cherry papaya tomato tomato' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #46 checking search results for 'pear kiwi banana pear cherry papaya tomato tomato' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #47 checking search results for 'orange fig tomato apple lime' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-378.html', 'title': 'N-378', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-185.html', 'title': 'N-185', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-859.html', 'title': 'N-859', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-533.html', 'title': 'N-533', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-544.html', 'title': 'N-544', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-390.html', 'title': 'N-390', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-793.html', 'title': 'N-793', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-908.html', 'title': 'N-908', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-844.html', 'title': 'N-844', 'score': 0.9983524765913274}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-286.html', 'title': 'N-286', 'score': 0.9983498505392223}]
result = search.search('orange fig tomato apple lime',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #47 checking search results for 'orange fig tomato apple lime' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #47 checking search results for 'orange fig tomato apple lime' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #48 checking search results for 'banana banana apple banana banana pear' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-923.html', 'title': 'N-923', 'score': 0.9992373906971392}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-221.html', 'title': 'N-221', 'score': 0.9990332064091457}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-512.html', 'title': 'N-512', 'score': 0.9990332064091457}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-754.html', 'title': 'N-754', 'score': 0.9990162794321004}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-268.html', 'title': 'N-268', 'score': 0.9989430777580094}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-799.html', 'title': 'N-799', 'score': 0.9989113661507846}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-75.html', 'title': 'N-75', 'score': 0.998702200732638}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-980.html', 'title': 'N-980', 'score': 0.9984443579922226}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-899.html', 'title': 'N-899', 'score': 0.998304859699232}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-21.html', 'title': 'N-21', 'score': 0.9948457774377981}]
result = search.search('banana banana apple banana banana pear',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #48 checking search results for 'banana banana apple banana banana pear' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #48 checking search results for 'banana banana apple banana banana pear' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #49 checking search results for 'coconut banana peach peach kiwi apricot coconut' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-448.html', 'title': 'N-448', 'score': 0.997022669642095}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-449.html', 'title': 'N-449', 'score': 0.9967104351812621}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-946.html', 'title': 'N-946', 'score': 0.9965653053353585}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-903.html', 'title': 'N-903', 'score': 0.9964782628583378}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-72.html', 'title': 'N-72', 'score': 0.9948921089663783}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-115.html', 'title': 'N-115', 'score': 0.9947835412300572}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-58.html', 'title': 'N-58', 'score': 0.9926215951851226}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-593.html', 'title': 'N-593', 'score': 0.9922187866202754}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-802.html', 'title': 'N-802', 'score': 0.9891034176375775}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-434.html', 'title': 'N-434', 'score': 0.9882135235869274}]
result = search.search('coconut banana peach peach kiwi apricot coconut',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #49 checking search results for 'coconut banana peach peach kiwi apricot coconut' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #49 checking search results for 'coconut banana peach peach kiwi apricot coconut' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


output.close()
success_output.close()
