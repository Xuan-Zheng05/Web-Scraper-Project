
import testingtools
import crawler
import searchdata
import search

#Performing crawl starting at seed http://people.scs.carleton.ca/~davidmckenney/fruits5/N-0.html
crawler.crawl('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-0.html')


output = open('fruits5-all-outgoing-failed.txt', 'w')
success_output = open('fruits5-all-outgoing-passed.txt', 'w')

#Test #0 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-636.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-907.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-128.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-625.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-636.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #0 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-636.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #0 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-636.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #1 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-476.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-7.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-476.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #1 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-476.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #1 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-476.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #2 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-367.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-107.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-266.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-467.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-367.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #2 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-367.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #2 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-367.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #3 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-792.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-501.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-792.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #3 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-792.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #3 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-792.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #4 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-271.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-4.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-411.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-750.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-271.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #4 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-271.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #4 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-271.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #5 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-366.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-153.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-375.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-461.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-577.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-626.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-824.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-969.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-74.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-444.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-366.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #5 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-366.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #5 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-366.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #6 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-221.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-83.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-221.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #6 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-221.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #6 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-221.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #7 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-495.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-28.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-53.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-432.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-495.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #7 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-495.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #7 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-495.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #8 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-904.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-177.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-904.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #8 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-904.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #8 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-904.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #9 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-477.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-79.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-922.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-477.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #9 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-477.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #9 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-477.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #10 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-860.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-860.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #10 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-860.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #10 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-860.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #11 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-90.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-172.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-379.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-443.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-550.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-858.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-0.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-63.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-100.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-111.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-169.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-364.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-372.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-503.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-545.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-90.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #11 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-90.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #11 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-90.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #12 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-92.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-295.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-682.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-3.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-251.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-92.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #12 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-92.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #12 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-92.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #13 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-519.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-146.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-519.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #13 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-519.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #13 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-519.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #14 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-597.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-788.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-597.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #14 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-597.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #14 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-597.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #15 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-717.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-224.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-717.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #15 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-717.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #15 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-717.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #16 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-808.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-0.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-808.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #16 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-808.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #16 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-808.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #17 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-12.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-0.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-20.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-94.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-97.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-119.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-201.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-338.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-578.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-839.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-6.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-25.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-29.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-127.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-142.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-147.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-178.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-241.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-282.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-316.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-422.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-834.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-837.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-12.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #17 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-12.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #17 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-12.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #18 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-634.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-563.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-634.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #18 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-634.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #18 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-634.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #19 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-762.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-421.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-762.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #19 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-762.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #19 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-762.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #20 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-460.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-463.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-91.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-736.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-914.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-460.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #20 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-460.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #20 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-460.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #21 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-0.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-1.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-3.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-6.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-7.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-11.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-14.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-23.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-33.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-42.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-53.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-59.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-60.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-80.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-85.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-87.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-90.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-100.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-114.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-121.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-138.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-148.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-190.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-207.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-212.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-231.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-239.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-298.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-327.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-373.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-378.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-407.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-429.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-433.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-437.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-451.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-457.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-572.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-638.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-666.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-675.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-767.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-843.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-921.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-939.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-4.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-9.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-12.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-21.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-26.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-30.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-34.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-41.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-43.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-44.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-47.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-56.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-72.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-88.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-109.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-124.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-130.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-135.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-150.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-151.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-155.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-169.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-196.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-202.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-211.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-218.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-256.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-278.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-297.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-382.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-387.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-399.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-411.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-420.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-423.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-517.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-528.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-555.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-556.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-621.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-633.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-639.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-651.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-716.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-808.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-823.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-829.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-870.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-954.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-966.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-973.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-991.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-0.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #21 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-0.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #21 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-0.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #22 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-80.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-105.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-124.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-210.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-670.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-902.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-0.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-40.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-606.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-80.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #22 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-80.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #22 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-80.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #23 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-265.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-10.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-273.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-718.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-870.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-97.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-438.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-481.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-265.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #23 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-265.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #23 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-265.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #24 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-67.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-32.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-184.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-67.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #24 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-67.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #24 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-67.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #25 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-865.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-653.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-215.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-865.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #25 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-865.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #25 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-865.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #26 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-206.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-14.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-155.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-206.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #26 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-206.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #26 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-206.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #27 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-321.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-512.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-73.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-321.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #27 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-321.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #27 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-321.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #28 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-633.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-0.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-633.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #28 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-633.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #28 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-633.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #29 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-514.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-183.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-514.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #29 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-514.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #29 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-514.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #30 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-616.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-196.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-616.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #30 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-616.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #30 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-616.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #31 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-574.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-89.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-768.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-574.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #31 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-574.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #31 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-574.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #32 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-176.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-54.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-150.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-161.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-294.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-635.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-930.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-176.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #32 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-176.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #32 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-176.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #33 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-436.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-406.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-436.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #33 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-436.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #33 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-436.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #34 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-428.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-3.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-428.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #34 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-428.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #34 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-428.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #35 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-652.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-11.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-652.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #35 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-652.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #35 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-652.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #36 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-304.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-19.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-130.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-233.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-473.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-479.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-304.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #36 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-304.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #36 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-304.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #37 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-622.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-822.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-967.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-224.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-596.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-622.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #37 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-622.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #37 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-622.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #38 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-134.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-204.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-289.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-19.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-73.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-115.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-780.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-134.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #38 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-134.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #38 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-134.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #39 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-995.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-222.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-995.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #39 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-995.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #39 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-995.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #40 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-916.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-9.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-916.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #40 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-916.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #40 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-916.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #41 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-926.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-368.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-926.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #41 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-926.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #41 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-926.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #42 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-985.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-195.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-606.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-985.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #42 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-985.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #42 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-985.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #43 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-355.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-604.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-60.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-445.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-566.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-773.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-883.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-355.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #43 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-355.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #43 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-355.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #44 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-645.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-115.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-211.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-877.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-4.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-645.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #44 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-645.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #44 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-645.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #45 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-727.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-51.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-55.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-697.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-727.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #45 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-727.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #45 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-727.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #46 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-692.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-311.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-318.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-861.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-21.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-711.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-692.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #46 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-692.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #46 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-692.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #47 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-308.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-48.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-105.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-382.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-453.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-204.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-311.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-643.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-308.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #47 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-308.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #47 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-308.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #48 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-651.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-0.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-94.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-651.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #48 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-651.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #48 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-651.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #49 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-908.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-63.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-908.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #49 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-908.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #49 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-908.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #50 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html
expected = None
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #50 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #50 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


output.close()
success_output.close()









output = open('fruits5-all-incoming-failed.txt', 'w')
success_output = open('fruits5-all-incoming-passed.txt', 'w')

#Test #51 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-970.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-472.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-731.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-970.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #51 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-970.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #51 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-970.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #52 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-111.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-90.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-572.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-101.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-168.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-217.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-583.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-522.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-562.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-712.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-903.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-942.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-111.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #52 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-111.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #52 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-111.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #53 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-149.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-466.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-101.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-63.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-520.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-149.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #53 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-149.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #53 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-149.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #54 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-986.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-107.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-928.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-986.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #54 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-986.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #54 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-986.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #55 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-743.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-715.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-743.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #55 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-743.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #55 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-743.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #56 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-966.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-0.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-966.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #56 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-966.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #56 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-966.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #57 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-778.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-626.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-778.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #57 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-778.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #57 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-778.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #58 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-14.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-0.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-10.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-125.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-523.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-333.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-206.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-932.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-89.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-189.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-521.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-953.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-14.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #58 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-14.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #58 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-14.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #59 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-820.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-433.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-870.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-51.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-820.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #59 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-820.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #59 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-820.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #60 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-989.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-555.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-989.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #60 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-989.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #60 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-989.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #61 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-448.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-69.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-448.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #61 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-448.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #61 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-448.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #62 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-405.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-105.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-250.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-694.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-405.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #62 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-405.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #62 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-405.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #63 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-953.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-14.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-953.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #63 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-953.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #63 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-953.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #64 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-144.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-44.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-76.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-589.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-406.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-131.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-144.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #64 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-144.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #64 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-144.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #65 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-710.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-66.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-299.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-710.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #65 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-710.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #65 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-710.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #66 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-395.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-104.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-395.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #66 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-395.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #66 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-395.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #67 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-201.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-12.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-805.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-755.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-801.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-255.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-201.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #67 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-201.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #67 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-201.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #68 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-597.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-788.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-597.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #68 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-597.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #68 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-597.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #69 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-337.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-10.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-22.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-337.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #69 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-337.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #69 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-337.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #70 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-327.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-0.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-219.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-15.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-413.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-359.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-598.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-485.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-689.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-354.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-950.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-327.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #70 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-327.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #70 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-327.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #71 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-319.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-3.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-319.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #71 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-319.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #71 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-319.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #72 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-768.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-574.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-768.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #72 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-768.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #72 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-768.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #73 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-659.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-462.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-659.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #73 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-659.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #73 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-659.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #74 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-117.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-72.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-313.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-217.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-266.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-66.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-330.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-852.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-468.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-516.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-758.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-117.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #74 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-117.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #74 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-117.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #75 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-76.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-69.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-144.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-562.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-125.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-76.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #75 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-76.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #75 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-76.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #76 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-829.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-0.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-298.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-383.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-191.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-829.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #76 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-829.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #76 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-829.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #77 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-588.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-735.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-22.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-588.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #77 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-588.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #77 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-588.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #78 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-729.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-65.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-49.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-729.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #78 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-729.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #78 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-729.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #79 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-595.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-13.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-595.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #79 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-595.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #79 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-595.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #80 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-542.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-153.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-86.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-975.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-542.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #80 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-542.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #80 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-542.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #81 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-293.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-281.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-761.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-293.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #81 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-293.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #81 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-293.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #82 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-411.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-0.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-282.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-271.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-411.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #82 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-411.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #82 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-411.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #83 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-278.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-0.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-41.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-215.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-455.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-278.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #83 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-278.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #83 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-278.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #84 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-236.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-28.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-889.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-168.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-236.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #84 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-236.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #84 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-236.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #85 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-108.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-4.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-541.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-108.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #85 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-108.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #85 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-108.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #86 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-896.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-297.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-333.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-896.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #86 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-896.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #86 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-896.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #87 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-130.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-0.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-196.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-387.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-304.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-233.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-13.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-98.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-188.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-335.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-510.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-130.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #87 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-130.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #87 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-130.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #88 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-718.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-265.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-718.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #88 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-718.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #88 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-718.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #89 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-268.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-254.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-141.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-962.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-268.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #89 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-268.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #89 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-268.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #90 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-537.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-39.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-126.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-537.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #90 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-537.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #90 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-537.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #91 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-912.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-53.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-912.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #91 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-912.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #91 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-912.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #92 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-88.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-0.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-53.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-168.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-178.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-613.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-36.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-27.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-626.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-385.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-620.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-167.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-487.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-88.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #92 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-88.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #92 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-88.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #93 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-954.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-0.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-954.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #93 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-954.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #93 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-954.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #94 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-493.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-859.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-32.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-69.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-493.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #94 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-493.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #94 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-493.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #95 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-254.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-63.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-806.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-268.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-515.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-752.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-825.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-312.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-568.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-254.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #95 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-254.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #95 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-254.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #96 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-640.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-430.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-640.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #96 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-640.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #96 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-640.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #97 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-520.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-739.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-625.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-63.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-316.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-149.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-738.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-520.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #97 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-520.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #97 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-520.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #98 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-563.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-3.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-10.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-634.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-563.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #98 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-563.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #98 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-563.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #99 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-538.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-178.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-538.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #99 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-538.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #99 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-538.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #100 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-481.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-150.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-265.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-235.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-481.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #100 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-481.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #100 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-481.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #101 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html
expected = None
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #101 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #101 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


output.close()
success_output.close()









output = open('fruits5-all-pagerank-failed.txt', 'w')
success_output = open('fruits5-all-pagerank-passed.txt', 'w')

#Test #102 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-870.html
expected = 0.0009102652798235549
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-870.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #102 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-870.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #102 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-870.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #103 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-843.html
expected = 0.0006326038069932237
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-843.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #103 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-843.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #103 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-843.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #104 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-760.html
expected = 0.0004394424366928165
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-760.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #104 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-760.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #104 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-760.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #105 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-345.html
expected = 0.0003591615108148512
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-345.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #105 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-345.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #105 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-345.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #106 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-499.html
expected = 0.0006325046863019859
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-499.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #106 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-499.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #106 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-499.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #107 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-952.html
expected = 0.0006756885451145058
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-952.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #107 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-952.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #107 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-952.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #108 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-39.html
expected = 0.005173257257766003
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-39.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #108 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-39.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #108 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-39.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #109 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-727.html
expected = 0.000904245120869892
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-727.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #109 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-727.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #109 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-727.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #110 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-341.html
expected = 0.0010970902226673685
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-341.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #110 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-341.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #110 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-341.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #111 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-795.html
expected = 0.0009088515944159108
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-795.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #111 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-795.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #111 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-795.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #112 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-630.html
expected = 0.0009452306368058312
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-630.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #112 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-630.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #112 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-630.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #113 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-671.html
expected = 0.00035925602547880794
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-671.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #113 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-671.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #113 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-671.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #114 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-637.html
expected = 0.00042024528340484324
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-637.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #114 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-637.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #114 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-637.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #115 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-604.html
expected = 0.0004352366610068793
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-604.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #115 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-604.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #115 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-604.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #116 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-333.html
expected = 0.0006684623599758046
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-333.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #116 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-333.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #116 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-333.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #117 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-123.html
expected = 0.0006509139710329609
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-123.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #117 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-123.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #117 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-123.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #118 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-352.html
expected = 0.0015257350814610105
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-352.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #118 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-352.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #118 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-352.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #119 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-726.html
expected = 0.00038854549750193625
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-726.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #119 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-726.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #119 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-726.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #120 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-924.html
expected = 0.00041408813686226947
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-924.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #120 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-924.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #120 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-924.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #121 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-243.html
expected = 0.0006742422578745172
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-243.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #121 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-243.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #121 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-243.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #122 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-391.html
expected = 0.0006513861223275382
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-391.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #122 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-391.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #122 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-391.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #123 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-937.html
expected = 0.0003734007226755988
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-937.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #123 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-937.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #123 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-937.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #124 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-300.html
expected = 0.000820707217890918
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-300.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #124 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-300.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #124 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-300.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #125 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-54.html
expected = 0.0015294087028559875
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-54.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #125 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-54.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #125 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-54.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #126 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-15.html
expected = 0.007741171716967465
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-15.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #126 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-15.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #126 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-15.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #127 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-670.html
expected = 0.0003649743439592553
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-670.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #127 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-670.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #127 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-670.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #128 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-99.html
expected = 0.0006124474971623658
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-99.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #128 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-99.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #128 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-99.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #129 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-861.html
expected = 0.0003878230988160015
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-861.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #129 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-861.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #129 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-861.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #130 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-530.html
expected = 0.00035474686013413495
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-530.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #130 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-530.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #130 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-530.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #131 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-956.html
expected = 0.00037000797455025635
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-956.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #131 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-956.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #131 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-956.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #132 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-375.html
expected = 0.00038520701546822527
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-375.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #132 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-375.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #132 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-375.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #133 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-822.html
expected = 0.0003884564221972197
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-822.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #133 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-822.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #133 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-822.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #134 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-738.html
expected = 0.001162506066095588
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-738.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #134 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-738.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #134 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-738.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #135 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-648.html
expected = 0.00035816970936534325
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-648.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #135 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-648.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #135 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-648.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #136 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-226.html
expected = 0.0003722418959316386
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-226.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #136 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-226.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #136 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-226.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #137 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-509.html
expected = 0.0011563680516523782
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-509.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #137 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-509.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #137 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-509.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #138 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-818.html
expected = 0.000918844716252041
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-818.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #138 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-818.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #138 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-818.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #139 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-954.html
expected = 0.00035714372225053464
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-954.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #139 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-954.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #139 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-954.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #140 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-920.html
expected = 0.0006743627530856482
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-920.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #140 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-920.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #140 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-920.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #141 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-272.html
expected = 0.000365912126428853
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-272.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #141 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-272.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #141 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-272.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #142 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-862.html
expected = 0.0006459606854050822
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-862.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #142 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-862.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #142 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-862.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #143 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-417.html
expected = 0.0008805851890034196
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-417.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #143 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-417.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #143 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-417.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #144 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-837.html
expected = 0.0014400791887984859
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-837.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #144 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-837.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #144 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-837.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #145 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-812.html
expected = 0.0003804539804548974
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-812.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #145 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-812.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #145 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-812.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #146 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-384.html
expected = 0.0007095954069363871
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-384.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #146 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-384.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #146 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-384.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #147 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-277.html
expected = 0.002000208044696688
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-277.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #147 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-277.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #147 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-277.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #148 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-741.html
expected = 0.00038538826320404874
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-741.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #148 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-741.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #148 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-741.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #149 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-20.html
expected = 0.00035332421321717554
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-20.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #149 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-20.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #149 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-20.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #150 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-164.html
expected = 0.0014179444854222146
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-164.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #150 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-164.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #150 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-164.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #151 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-197.html
expected = 0.001079591593515207
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-197.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #151 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-197.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #151 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-197.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #152 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html
expected = -1
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #152 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #152 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


output.close()
success_output.close()









output = open('fruits5-all-idf-failed.txt', 'w')
success_output = open('fruits5-all-idf-passed.txt', 'w')

#Test #153 checking IDF for word blueberry
expected = 0.1729939903610231
result = searchdata.get_idf('blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #153 checking IDF for word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #153 checking IDF for word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #154 checking IDF for word banana
expected = 0.16326791954086414
result = searchdata.get_idf('banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #154 checking IDF for word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #154 checking IDF for word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #155 checking IDF for word cherry
expected = 0.15682010974282581
result = searchdata.get_idf('cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #155 checking IDF for word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #155 checking IDF for word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #156 checking IDF for word pear
expected = 0.16812275880832706
result = searchdata.get_idf('pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #156 checking IDF for word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #156 checking IDF for word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #157 checking IDF for word papaya
expected = 0.16650266314016507
result = searchdata.get_idf('papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #157 checking IDF for word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #157 checking IDF for word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #158 checking IDF for word apricot
expected = 0.1729939903610231
result = searchdata.get_idf('apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #158 checking IDF for word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #158 checking IDF for word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #159 checking IDF for word orange
expected = 0.16650266314016507
result = searchdata.get_idf('orange')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #159 checking IDF for word orange\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #159 checking IDF for word orange\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #160 checking IDF for word peach
expected = 0.1600404125104682
result = searchdata.get_idf('peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #160 checking IDF for word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #160 checking IDF for word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #161 checking IDF for word fig
expected = 0.16650266314016507
result = searchdata.get_idf('fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #161 checking IDF for word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #161 checking IDF for word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #162 checking IDF for word lime
expected = 0.16326791954086414
result = searchdata.get_idf('lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #162 checking IDF for word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #162 checking IDF for word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #163 checking IDF for word kiwi
expected = 0.1729939903610231
result = searchdata.get_idf('kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #163 checking IDF for word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #163 checking IDF for word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #164 checking IDF for word coconut
expected = 0.1600404125104682
result = searchdata.get_idf('coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #164 checking IDF for word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #164 checking IDF for word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #165 checking IDF for word apple
expected = 0.15521264992094008
result = searchdata.get_idf('apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #165 checking IDF for word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #165 checking IDF for word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #166 checking IDF for word tomato
expected = 0
result = searchdata.get_idf('tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #166 checking IDF for word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #166 checking IDF for word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


output.close()
success_output.close()









output = open('fruits5-all-tf-failed.txt', 'w')
success_output = open('fruits5-all-tf-passed.txt', 'w')

#Test #167 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-78.html and word papaya
expected = 0.03488372093023256
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-78.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #167 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-78.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #167 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-78.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #168 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-78.html and word cherry
expected = 0.11627906976744186
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-78.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #168 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-78.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #168 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-78.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #169 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-78.html and word apple
expected = 0.03488372093023256
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-78.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #169 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-78.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #169 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-78.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #170 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-78.html and word coconut
expected = 0.06976744186046512
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-78.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #170 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-78.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #170 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-78.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #171 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-78.html and word apricot
expected = 0.09302325581395349
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-78.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #171 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-78.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #171 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-78.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #172 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-78.html and word fig
expected = 0.05813953488372093
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-78.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #172 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-78.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #172 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-78.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #173 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-78.html and word peach
expected = 0.09302325581395349
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-78.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #173 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-78.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #173 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-78.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #174 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-78.html and word lime
expected = 0.11627906976744186
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-78.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #174 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-78.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #174 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-78.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #175 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-78.html and word banana
expected = 0.046511627906976744
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-78.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #175 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-78.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #175 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-78.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #176 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-78.html and word pear
expected = 0.08139534883720931
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-78.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #176 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-78.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #176 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-78.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #177 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-78.html and word tomato
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-78.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #177 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-78.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #177 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-78.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #178 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-617.html and word papaya
expected = 0.02702702702702703
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-617.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #178 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-617.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #178 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-617.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #179 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-617.html and word cherry
expected = 0.08108108108108109
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-617.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #179 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-617.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #179 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-617.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #180 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-617.html and word apple
expected = 0.08108108108108109
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-617.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #180 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-617.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #180 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-617.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #181 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-617.html and word coconut
expected = 0.08108108108108109
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-617.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #181 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-617.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #181 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-617.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #182 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-617.html and word apricot
expected = 0.16216216216216217
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-617.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #182 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-617.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #182 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-617.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #183 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-617.html and word fig
expected = 0.05405405405405406
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-617.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #183 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-617.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #183 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-617.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #184 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-617.html and word peach
expected = 0.08108108108108109
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-617.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #184 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-617.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #184 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-617.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #185 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-617.html and word lime
expected = 0.08108108108108109
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-617.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #185 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-617.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #185 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-617.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #186 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-617.html and word banana
expected = 0.08108108108108109
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-617.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #186 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-617.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #186 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-617.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #187 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-617.html and word pear
expected = 0.08108108108108109
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-617.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #187 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-617.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #187 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-617.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #188 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-617.html and word tomato
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-617.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #188 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-617.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #188 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-617.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #189 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-395.html and word papaya
expected = 0.06521739130434782
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-395.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #189 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-395.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #189 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-395.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #190 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-395.html and word cherry
expected = 0.10869565217391304
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-395.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #190 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-395.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #190 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-395.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #191 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-395.html and word apple
expected = 0.10869565217391304
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-395.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #191 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-395.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #191 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-395.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #192 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-395.html and word coconut
expected = 0.06521739130434782
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-395.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #192 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-395.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #192 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-395.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #193 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-395.html and word apricot
expected = 0.043478260869565216
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-395.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #193 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-395.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #193 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-395.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #194 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-395.html and word fig
expected = 0.06521739130434782
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-395.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #194 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-395.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #194 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-395.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #195 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-395.html and word peach
expected = 0.08695652173913043
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-395.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #195 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-395.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #195 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-395.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #196 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-395.html and word lime
expected = 0.17391304347826086
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-395.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #196 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-395.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #196 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-395.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #197 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-395.html and word banana
expected = 0.08695652173913043
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-395.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #197 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-395.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #197 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-395.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #198 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-395.html and word pear
expected = 0.021739130434782608
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-395.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #198 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-395.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #198 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-395.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #199 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-395.html and word tomato
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-395.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #199 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-395.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #199 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-395.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #200 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-90.html and word papaya
expected = 0.05263157894736842
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-90.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #200 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-90.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #200 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-90.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #201 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-90.html and word cherry
expected = 0.05263157894736842
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-90.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #201 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-90.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #201 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-90.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #202 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-90.html and word apple
expected = 0.10526315789473684
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-90.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #202 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-90.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #202 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-90.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #203 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-90.html and word coconut
expected = 0.05263157894736842
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-90.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #203 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-90.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #203 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-90.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #204 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-90.html and word apricot
expected = 0.05263157894736842
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-90.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #204 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-90.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #204 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-90.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #205 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-90.html and word fig
expected = 0.10526315789473684
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-90.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #205 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-90.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #205 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-90.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #206 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-90.html and word peach
expected = 0.05263157894736842
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-90.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #206 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-90.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #206 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-90.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #207 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-90.html and word lime
expected = 0.05263157894736842
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-90.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #207 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-90.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #207 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-90.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #208 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-90.html and word banana
expected = 0.10526315789473684
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-90.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #208 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-90.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #208 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-90.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #209 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-90.html and word pear
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-90.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #209 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-90.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #209 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-90.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #210 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-90.html and word tomato
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-90.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #210 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-90.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #210 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-90.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #211 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-306.html and word papaya
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-306.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #211 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-306.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #211 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-306.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #212 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-306.html and word cherry
expected = 0.07692307692307693
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-306.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #212 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-306.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #212 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-306.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #213 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-306.html and word apple
expected = 0.07692307692307693
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-306.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #213 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-306.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #213 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-306.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #214 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-306.html and word coconut
expected = 0.07692307692307693
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-306.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #214 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-306.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #214 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-306.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #215 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-306.html and word apricot
expected = 0.07692307692307693
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-306.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #215 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-306.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #215 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-306.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #216 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-306.html and word fig
expected = 0.07692307692307693
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-306.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #216 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-306.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #216 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-306.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #217 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-306.html and word peach
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-306.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #217 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-306.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #217 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-306.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #218 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-306.html and word lime
expected = 0.07692307692307693
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-306.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #218 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-306.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #218 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-306.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #219 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-306.html and word banana
expected = 0.07692307692307693
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-306.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #219 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-306.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #219 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-306.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #220 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-306.html and word pear
expected = 0.15384615384615385
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-306.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #220 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-306.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #220 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-306.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #221 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-306.html and word tomato
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-306.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #221 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-306.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #221 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-306.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #222 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-488.html and word papaya
expected = 0.14285714285714285
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-488.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #222 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-488.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #222 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-488.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #223 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-488.html and word cherry
expected = 0.14285714285714285
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-488.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #223 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-488.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #223 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-488.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #224 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-488.html and word apple
expected = 0.047619047619047616
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-488.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #224 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-488.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #224 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-488.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #225 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-488.html and word coconut
expected = 0.047619047619047616
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-488.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #225 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-488.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #225 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-488.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #226 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-488.html and word apricot
expected = 0.047619047619047616
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-488.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #226 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-488.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #226 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-488.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #227 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-488.html and word fig
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-488.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #227 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-488.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #227 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-488.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #228 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-488.html and word peach
expected = 0.09523809523809523
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-488.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #228 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-488.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #228 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-488.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #229 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-488.html and word lime
expected = 0.047619047619047616
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-488.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #229 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-488.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #229 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-488.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #230 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-488.html and word banana
expected = 0.23809523809523808
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-488.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #230 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-488.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #230 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-488.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #231 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-488.html and word pear
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-488.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #231 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-488.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #231 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-488.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #232 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-488.html and word tomato
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-488.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #232 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-488.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #232 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-488.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #233 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-693.html and word papaya
expected = 0.0784313725490196
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-693.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #233 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-693.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #233 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-693.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #234 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-693.html and word cherry
expected = 0.11764705882352941
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-693.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #234 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-693.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #234 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-693.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #235 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-693.html and word apple
expected = 0.0784313725490196
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-693.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #235 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-693.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #235 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-693.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #236 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-693.html and word coconut
expected = 0.058823529411764705
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-693.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #236 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-693.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #236 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-693.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #237 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-693.html and word apricot
expected = 0.09803921568627451
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-693.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #237 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-693.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #237 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-693.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #238 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-693.html and word fig
expected = 0.0392156862745098
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-693.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #238 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-693.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #238 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-693.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #239 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-693.html and word peach
expected = 0.0784313725490196
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-693.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #239 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-693.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #239 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-693.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #240 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-693.html and word lime
expected = 0.058823529411764705
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-693.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #240 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-693.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #240 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-693.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #241 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-693.html and word banana
expected = 0.11764705882352941
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-693.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #241 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-693.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #241 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-693.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #242 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-693.html and word pear
expected = 0.13725490196078433
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-693.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #242 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-693.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #242 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-693.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #243 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-693.html and word tomato
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-693.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #243 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-693.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #243 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-693.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #244 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-315.html and word papaya
expected = 0.10256410256410256
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-315.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #244 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-315.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #244 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-315.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #245 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-315.html and word cherry
expected = 0.02564102564102564
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-315.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #245 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-315.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #245 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-315.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #246 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-315.html and word apple
expected = 0.07692307692307693
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-315.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #246 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-315.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #246 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-315.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #247 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-315.html and word coconut
expected = 0.14102564102564102
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-315.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #247 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-315.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #247 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-315.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #248 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-315.html and word apricot
expected = 0.07692307692307693
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-315.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #248 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-315.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #248 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-315.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #249 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-315.html and word fig
expected = 0.07692307692307693
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-315.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #249 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-315.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #249 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-315.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #250 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-315.html and word peach
expected = 0.07692307692307693
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-315.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #250 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-315.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #250 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-315.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #251 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-315.html and word lime
expected = 0.0641025641025641
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-315.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #251 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-315.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #251 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-315.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #252 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-315.html and word banana
expected = 0.0641025641025641
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-315.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #252 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-315.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #252 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-315.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #253 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-315.html and word pear
expected = 0.08974358974358974
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-315.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #253 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-315.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #253 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-315.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #254 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-315.html and word tomato
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-315.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #254 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-315.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #254 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-315.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #255 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-786.html and word papaya
expected = 0.09302325581395349
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-786.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #255 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-786.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #255 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-786.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #256 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-786.html and word cherry
expected = 0.046511627906976744
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-786.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #256 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-786.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #256 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-786.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #257 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-786.html and word apple
expected = 0.023255813953488372
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-786.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #257 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-786.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #257 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-786.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #258 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-786.html and word coconut
expected = 0.11627906976744186
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-786.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #258 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-786.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #258 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-786.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #259 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-786.html and word apricot
expected = 0.09302325581395349
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-786.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #259 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-786.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #259 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-786.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #260 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-786.html and word fig
expected = 0.13953488372093023
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-786.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #260 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-786.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #260 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-786.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #261 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-786.html and word peach
expected = 0.06976744186046512
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-786.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #261 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-786.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #261 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-786.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #262 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-786.html and word lime
expected = 0.13953488372093023
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-786.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #262 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-786.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #262 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-786.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #263 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-786.html and word banana
expected = 0.046511627906976744
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-786.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #263 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-786.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #263 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-786.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #264 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-786.html and word pear
expected = 0.09302325581395349
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-786.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #264 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-786.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #264 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-786.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #265 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-786.html and word tomato
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-786.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #265 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-786.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #265 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-786.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #266 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-965.html and word papaya
expected = 0.1111111111111111
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-965.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #266 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-965.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #266 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-965.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #267 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-965.html and word cherry
expected = 0.05555555555555555
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-965.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #267 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-965.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #267 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-965.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #268 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-965.html and word apple
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-965.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #268 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-965.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #268 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-965.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #269 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-965.html and word coconut
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-965.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #269 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-965.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #269 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-965.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #270 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-965.html and word apricot
expected = 0.2222222222222222
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-965.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #270 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-965.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #270 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-965.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #271 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-965.html and word fig
expected = 0.05555555555555555
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-965.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #271 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-965.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #271 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-965.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #272 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-965.html and word peach
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-965.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #272 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-965.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #272 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-965.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #273 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-965.html and word lime
expected = 0.05555555555555555
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-965.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #273 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-965.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #273 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-965.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #274 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-965.html and word banana
expected = 0.2222222222222222
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-965.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #274 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-965.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #274 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-965.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #275 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-965.html and word pear
expected = 0.05555555555555555
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-965.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #275 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-965.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #275 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-965.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #276 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-965.html and word tomato
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-965.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #276 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-965.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #276 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-965.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #277 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word papaya
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #277 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #277 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #278 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word cherry
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #278 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #278 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #279 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word apple
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #279 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #279 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #280 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word coconut
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #280 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #280 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #281 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word apricot
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #281 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #281 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #282 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word fig
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #282 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #282 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #283 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word peach
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #283 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #283 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #284 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word lime
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #284 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #284 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #285 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word banana
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #285 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #285 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #286 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word pear
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #286 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #286 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #287 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word tomato
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #287 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #287 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


output.close()
success_output.close()









output = open('fruits5-all-tfidf-failed.txt', 'w')
success_output = open('fruits5-all-tfidf-passed.txt', 'w')

#Test #288 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-882.html and word blueberry
expected = 0.014949232742962176
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-882.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #288 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-882.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #288 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-882.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #289 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-882.html and word orange
expected = 0.03058852945388391
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-882.html','orange')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #289 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-882.html and word orange\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #289 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-882.html and word orange\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #290 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-882.html and word pear
expected = 0.020104391143096593
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-882.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #290 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-882.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #290 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-882.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #291 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-882.html and word kiwi
expected = 0.020686900882873387
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-882.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #291 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-882.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #291 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-882.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #292 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-882.html and word apricot
expected = 0.023507016447801017
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-882.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #292 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-882.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #292 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-882.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #293 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-882.html and word banana
expected = 0.011353803495159985
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-882.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #293 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-882.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #293 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-882.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #294 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-882.html and word coconut
expected = 0.036810191975349515
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-882.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #294 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-882.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #294 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-882.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #295 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-882.html and word lime
expected = 0.014108756746878972
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-882.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #295 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-882.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #295 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-882.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #296 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-882.html and word cherry
expected = 0.0027760298545087404
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-882.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #296 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-882.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #296 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-882.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #297 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-882.html and word papaya
expected = 0.008735965140466836
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-882.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #297 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-882.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #297 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-882.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #298 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-882.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-882.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #298 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-882.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #298 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-882.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #299 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-55.html and word blueberry
expected = 0.016107367405820545
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-55.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #299 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-55.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #299 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-55.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #300 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-55.html and word orange
expected = 0.01848700920467347
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-55.html','orange')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #300 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-55.html and word orange\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #300 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-55.html and word orange\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #301 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-55.html and word pear
expected = 0.018666890552904814
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-55.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #301 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-55.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #301 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-55.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #302 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-55.html and word kiwi
expected = 0.025295309433367146
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-55.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #302 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-55.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #302 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-55.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #303 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-55.html and word apricot
expected = 0.016107367405820545
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-55.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #303 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-55.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #303 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-55.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #304 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-55.html and word banana
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-55.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #304 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-55.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #304 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-55.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #305 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-55.html and word coconut
expected = 0.023401227683387336
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-55.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #305 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-55.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #305 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-55.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #306 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-55.html and word lime
expected = 0.018127851377602
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-55.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #306 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-55.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #306 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-55.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #307 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-55.html and word cherry
expected = 0.00887343512805005
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-55.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #307 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-55.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #307 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-55.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #308 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-55.html and word papaya
expected = 0.015502963794576245
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-55.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #308 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-55.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #308 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-55.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #309 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-55.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-55.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #309 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-55.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #309 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-55.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #310 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-120.html and word blueberry
expected = 0.025841431253021522
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-120.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #310 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-120.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #310 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-120.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #311 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-120.html and word orange
expected = 0.0043282714496191785
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-120.html','orange')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #311 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-120.html and word orange\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #311 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-120.html and word orange\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #312 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-120.html and word pear
expected = 0.017028033842257286
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-120.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #312 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-120.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #312 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-120.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #313 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-120.html and word kiwi
expected = 0.017521408423549677
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-120.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #313 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-120.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #313 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-120.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #314 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-120.html and word apricot
expected = 0.025841431253021522
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-120.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #314 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-120.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #314 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-120.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #315 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-120.html and word banana
expected = 0.008413244978821463
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-120.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #315 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-120.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #315 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-120.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #316 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-120.html and word coconut
expected = 0.016209426847818845
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-120.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #316 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-120.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #316 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-120.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #317 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-120.html and word lime
expected = 0.004244183615204744
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-120.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #317 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-120.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #317 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-120.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #318 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-120.html and word cherry
expected = 0.03072422882915727
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-120.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #318 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-120.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #318 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-120.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #319 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-120.html and word papaya
expected = 0.028777753665641982
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-120.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #319 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-120.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #319 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-120.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #320 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-120.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-120.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #320 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-120.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #320 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-120.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #321 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-252.html and word blueberry
expected = 0.03059878986905253
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-252.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #321 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-252.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #321 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-252.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #322 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-252.html and word orange
expected = 0.01271262587377561
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-252.html','orange')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #322 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-252.html and word orange\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #322 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-252.html and word orange\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #323 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-252.html and word pear
expected = 0.017786490782679056
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-252.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #323 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-252.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #323 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-252.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #324 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-252.html and word kiwi
expected = 0.013208244459248656
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-252.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #324 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-252.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #324 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-252.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #325 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-252.html and word apricot
expected = 0.015768036868167072
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-252.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #325 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-252.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #325 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-252.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #326 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-252.html and word banana
expected = 0.014881526053805143
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-252.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #326 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-252.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #326 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-252.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #327 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-252.html and word coconut
expected = 0.021549365796572184
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-252.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #327 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-252.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #327 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-252.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #328 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-252.html and word lime
expected = 0.01002473918599058
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-252.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #328 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-252.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #328 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-252.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #329 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-252.html and word cherry
expected = 0.007259775629994683
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-252.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #329 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-252.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #329 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-252.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #330 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-252.html and word papaya
expected = 0.015176366101291187
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-252.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #330 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-252.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #330 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-252.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #331 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-252.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-252.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #331 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-252.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #331 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-252.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #332 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-472.html and word blueberry
expected = 0.019976864637262157
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-472.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #332 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-472.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #332 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-472.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #333 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-472.html and word orange
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-472.html','orange')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #333 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-472.html and word orange\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #333 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-472.html and word orange\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #334 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-472.html and word pear
expected = 0.0373892274131475
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-472.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #334 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-472.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #334 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-472.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #335 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-472.html and word kiwi
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-472.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #335 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-472.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #335 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-472.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #336 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-472.html and word apricot
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-472.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #336 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-472.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #336 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-472.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #337 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-472.html and word banana
expected = 0.018853725042520968
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-472.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #337 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-472.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #337 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-472.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #338 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-472.html and word coconut
expected = 0.03559177484988699
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-472.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #338 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-472.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #338 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-472.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #339 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-472.html and word lime
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-472.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #339 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-472.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #339 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-472.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #340 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-472.html and word cherry
expected = 0.034875603919954534
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-472.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #340 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-472.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #340 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-472.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #341 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-472.html and word papaya
expected = 0.019227264232435187
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-472.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #341 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-472.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #341 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-472.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #342 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-472.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-472.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #342 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-472.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #342 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-472.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #343 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-495.html and word blueberry
expected = 0.009187942027546615
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-495.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #343 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-495.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #343 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-495.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #344 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-495.html and word orange
expected = 0.014562795993986995
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-495.html','orange')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #344 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-495.html and word orange\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #344 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-495.html and word orange\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #345 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-495.html and word pear
expected = 0.020345443067920698
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-495.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #345 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-495.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #345 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-495.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #346 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-495.html and word kiwi
expected = 0.020934937107445865
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-495.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #346 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-495.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #346 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-495.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #347 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-495.html and word apricot
expected = 0.018049615122291703
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-495.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #347 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-495.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #347 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-495.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #348 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-495.html and word banana
expected = 0.019757932747365693
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-495.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #348 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-495.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #348 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-495.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #349 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-495.html and word coconut
expected = 0.013997589193041912
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-495.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #349 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-495.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #349 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-495.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #350 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-495.html and word lime
expected = 0.025111477235907533
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-495.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #350 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-495.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #350 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-495.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #351 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-495.html and word cherry
expected = 0.021563317684490064
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-495.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #351 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-495.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #351 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-495.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #352 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-495.html and word papaya
expected = 0.017372331722302906
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-495.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #352 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-495.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #352 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-495.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #353 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-495.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-495.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #353 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-495.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #353 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-495.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #354 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-263.html and word blueberry
expected = 0.011094162973435432
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-263.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #354 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-263.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #354 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-263.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #355 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-263.html and word orange
expected = 0.02090122617329653
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-263.html','orange')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #355 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-263.html and word orange\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #355 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-263.html and word orange\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #356 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-263.html and word pear
expected = 0.010781769250311471
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-263.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #356 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-263.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #356 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-263.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #357 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-263.html and word kiwi
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-263.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #357 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-263.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #357 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-263.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #358 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-263.html and word apricot
expected = 0.0217160882052258
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-263.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #358 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-263.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #358 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-263.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #359 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-263.html and word banana
expected = 0.010470426769970589
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-263.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #359 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-263.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #359 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-263.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #360 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-263.html and word coconut
expected = 0.020090014151503705
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-263.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #360 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-263.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #360 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-263.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #361 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-263.html and word lime
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-263.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #361 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-263.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #361 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-263.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #362 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-263.html and word cherry
expected = 0.03779491661309501
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-263.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #362 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-263.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #362 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-263.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #363 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-263.html and word papaya
expected = 0.040128490405731757
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-263.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #363 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-263.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #363 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-263.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #364 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-263.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-263.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #364 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-263.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #364 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-263.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #365 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-927.html and word blueberry
expected = 0.013493965809283838
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-927.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #365 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-927.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #365 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-927.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #366 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-927.html and word orange
expected = 0.0161277042414117
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-927.html','orange')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #366 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-927.html and word orange\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #366 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-927.html and word orange\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #367 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-927.html and word pear
expected = 0.019414348372148626
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-927.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #367 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-927.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #367 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-927.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #368 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-927.html and word kiwi
expected = 0.032458343978857024
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-927.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #368 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-927.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #368 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-927.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #369 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-927.html and word apricot
expected = 0.016756464187816237
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-927.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #369 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-927.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #369 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-927.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #370 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-927.html and word banana
expected = 0.018853725042520968
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-927.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #370 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-927.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #370 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-927.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #371 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-927.html and word coconut
expected = 0.012483554197536504
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-927.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #371 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-927.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #371 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-927.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #372 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-927.html and word lime
expected = 0.018853725042520968
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-927.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #372 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-927.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #372 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-927.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #373 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-927.html and word cherry
expected = 0.020991272892657776
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-927.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #373 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-927.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #373 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-927.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #374 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-927.html and word papaya
expected = 0.019227264232435187
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-927.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #374 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-927.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #374 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-927.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #375 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-927.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-927.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #375 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-927.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #375 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-927.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #376 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-638.html and word blueberry
expected = 0.024978586583758202
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-638.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #376 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-638.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #376 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-638.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #377 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-638.html and word orange
expected = 0.02019782137665499
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-638.html','orange')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #377 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-638.html and word orange\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #377 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-638.html and word orange\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #378 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-638.html and word pear
expected = 0.012441181905748045
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-638.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #378 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-638.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #378 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-638.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #379 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-638.html and word kiwi
expected = 0.020985260239383192
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-638.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #379 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-638.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #379 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-638.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #380 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-638.html and word apricot
expected = 0.016926998920790533
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-638.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #380 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-638.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #380 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-638.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #381 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-638.html and word banana
expected = 0.01980542661139554
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-638.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #381 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-638.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #381 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-638.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #382 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-638.html and word coconut
expected = 0.007962496276591685
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-638.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #382 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-638.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #382 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-638.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #383 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-638.html and word lime
expected = 0.01208192097713971
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-638.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #383 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-638.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #383 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-638.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #384 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-638.html and word cherry
expected = 0.022643241427698756
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-638.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #384 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-638.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #384 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-638.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #385 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-638.html and word papaya
expected = 0.01629183992692806
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-638.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #385 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-638.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #385 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-638.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #386 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-638.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-638.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #386 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-638.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #386 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-638.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #387 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-953.html and word blueberry
expected = 0.03332644075666537
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-953.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #387 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-953.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #387 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-953.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #388 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-953.html and word orange
expected = 0.032075918518253574
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-953.html','orange')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #388 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-953.html and word orange\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #388 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-953.html and word orange\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #389 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-953.html and word pear
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-953.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #389 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-953.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #389 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-953.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #390 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-953.html and word kiwi
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-953.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #390 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-953.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #390 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-953.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #391 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-953.html and word apricot
expected = 0.017219073350844823
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-953.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #391 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-953.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #391 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-953.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #392 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-953.html and word banana
expected = 0.016250982340756406
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-953.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #392 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-953.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #392 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-953.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #393 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-953.html and word coconut
expected = 0.015929730254595636
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-953.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #393 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-953.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #393 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-953.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #394 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-953.html and word lime
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-953.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #394 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-953.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #394 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-953.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #395 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-953.html and word cherry
expected = 0.015609195249580477
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-953.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #395 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-953.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #395 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-953.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #396 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-953.html and word papaya
expected = 0.016572954723677334
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-953.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #396 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-953.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #396 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-953.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #397 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-953.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-953.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #397 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-953.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #397 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-953.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #398 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word blueberry
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #398 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #398 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #399 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word orange
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','orange')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #399 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word orange\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #399 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word orange\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #400 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word pear
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #400 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #400 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #401 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word kiwi
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #401 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #401 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #402 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word apricot
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #402 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #402 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #403 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word banana
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #403 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #403 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #404 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word coconut
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #404 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #404 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #405 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word lime
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #405 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #405 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #406 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word cherry
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #406 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #406 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #407 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word papaya
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #407 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #407 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #408 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #408 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #408 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


output.close()
success_output.close()









output = open('fruits5-all-search-failed.txt', 'w')
success_output = open('fruits5-all-search-passed.txt', 'w')

#Test #409 checking search results for 'apple kiwi banana orange banana' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-789.html', 'title': 'N-789', 'score': 0.9996942387021109}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-390.html', 'title': 'N-390', 'score': 0.9996512810071314}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-908.html', 'title': 'N-908', 'score': 0.9996323133609581}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-653.html', 'title': 'N-653', 'score': 0.9996147942669175}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-106.html', 'title': 'N-106', 'score': 0.999590914369144}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-884.html', 'title': 'N-884', 'score': 0.9995695382221392}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-247.html', 'title': 'N-247', 'score': 0.9994629183548798}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-938.html', 'title': 'N-938', 'score': 0.998239158014846}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-387.html', 'title': 'N-387', 'score': 0.9979020170111078}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-931.html', 'title': 'N-931', 'score': 0.9977841250353163}]
result = search.search('apple kiwi banana orange banana',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #409 checking search results for 'apple kiwi banana orange banana' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #409 checking search results for 'apple kiwi banana orange banana' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #410 checking search results for 'papaya apple papaya cherry pear apple tomato' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-588.html', 'title': 'N-588', 'score': 0.9999281315829682}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-718.html', 'title': 'N-718', 'score': 0.9993562429854479}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-7.html', 'title': 'N-7', 'score': 0.9979572486125914}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-445.html', 'title': 'N-445', 'score': 0.9970238121528153}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-115.html', 'title': 'N-115', 'score': 0.9968697343085934}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-149.html', 'title': 'N-149', 'score': 0.9961082100395873}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-562.html', 'title': 'N-562', 'score': 0.9957269331176338}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-629.html', 'title': 'N-629', 'score': 0.9945809698722032}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-570.html', 'title': 'N-570', 'score': 0.9943791713265181}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-596.html', 'title': 'N-596', 'score': 0.9942706186647955}]
result = search.search('papaya apple papaya cherry pear apple tomato',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #410 checking search results for 'papaya apple papaya cherry pear apple tomato' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #410 checking search results for 'papaya apple papaya cherry pear apple tomato' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #411 checking search results for 'papaya apricot cherry cherry fig peach apricot' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-281.html', 'title': 'N-281', 'score': 0.9998856895792398}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-675.html', 'title': 'N-675', 'score': 0.995320075727367}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-429.html', 'title': 'N-429', 'score': 0.9934299918727576}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-353.html', 'title': 'N-353', 'score': 0.9930231880557586}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-486.html', 'title': 'N-486', 'score': 0.9929524178736303}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-702.html', 'title': 'N-702', 'score': 0.991669712400663}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-424.html', 'title': 'N-424', 'score': 0.9916547254029405}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-244.html', 'title': 'N-244', 'score': 0.9916211994710464}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-972.html', 'title': 'N-972', 'score': 0.9912901325842011}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-79.html', 'title': 'N-79', 'score': 0.9909252196378837}]
result = search.search('papaya apricot cherry cherry fig peach apricot',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #411 checking search results for 'papaya apricot cherry cherry fig peach apricot' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #411 checking search results for 'papaya apricot cherry cherry fig peach apricot' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #412 checking search results for 'banana kiwi coconut blueberry cherry kiwi orange' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-542.html', 'title': 'N-542', 'score': 0.9960248722603241}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-814.html', 'title': 'N-814', 'score': 0.9912424584483416}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-736.html', 'title': 'N-736', 'score': 0.9901875296616074}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-149.html', 'title': 'N-149', 'score': 0.9890924971741274}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-300.html', 'title': 'N-300', 'score': 0.9875130624435335}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-927.html', 'title': 'N-927', 'score': 0.9873170878725408}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-401.html', 'title': 'N-401', 'score': 0.9867619773230332}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-652.html', 'title': 'N-652', 'score': 0.9864858885523285}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-406.html', 'title': 'N-406', 'score': 0.9858467492824403}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-385.html', 'title': 'N-385', 'score': 0.9857794798612469}]
result = search.search('banana kiwi coconut blueberry cherry kiwi orange',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #412 checking search results for 'banana kiwi coconut blueberry cherry kiwi orange' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #412 checking search results for 'banana kiwi coconut blueberry cherry kiwi orange' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #413 checking search results for 'banana apricot kiwi kiwi apricot coconut peach blueberry' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-40.html', 'title': 'N-40', 'score': 0.9998966674285452}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-635.html', 'title': 'N-635', 'score': 0.9967940418910423}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-430.html', 'title': 'N-430', 'score': 0.9953524938421694}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-652.html', 'title': 'N-652', 'score': 0.9939083600802361}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-406.html', 'title': 'N-406', 'score': 0.9918076621098052}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-675.html', 'title': 'N-675', 'score': 0.9878353863586687}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-588.html', 'title': 'N-588', 'score': 0.9871949178666706}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-736.html', 'title': 'N-736', 'score': 0.9857121301941936}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-233.html', 'title': 'N-233', 'score': 0.9854892214986366}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-720.html', 'title': 'N-720', 'score': 0.9851350495326786}]
result = search.search('banana apricot kiwi kiwi apricot coconut peach blueberry',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #413 checking search results for 'banana apricot kiwi kiwi apricot coconut peach blueberry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #413 checking search results for 'banana apricot kiwi kiwi apricot coconut peach blueberry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #414 checking search results for 'coconut orange pear fig kiwi tomato fig tomato' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-106.html', 'title': 'N-106', 'score': 0.9998787090020426}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-80.html', 'title': 'N-80', 'score': 0.9928360431070967}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-256.html', 'title': 'N-256', 'score': 0.9905361829378356}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-730.html', 'title': 'N-730', 'score': 0.9903654503054544}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-637.html', 'title': 'N-637', 'score': 0.9897173946877965}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-407.html', 'title': 'N-407', 'score': 0.9894899214832416}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-55.html', 'title': 'N-55', 'score': 0.9888389994818564}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-415.html', 'title': 'N-415', 'score': 0.9887362813377721}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-714.html', 'title': 'N-714', 'score': 0.9885307509415597}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-371.html', 'title': 'N-371', 'score': 0.9872951668548372}]
result = search.search('coconut orange pear fig kiwi tomato fig tomato',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #414 checking search results for 'coconut orange pear fig kiwi tomato fig tomato' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #414 checking search results for 'coconut orange pear fig kiwi tomato fig tomato' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #415 checking search results for 'lime lime papaya apricot apple tomato peach blueberry' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-158.html', 'title': 'N-158', 'score': 0.9931123207439766}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-750.html', 'title': 'N-750', 'score': 0.9900327276865496}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-24.html', 'title': 'N-24', 'score': 0.9898847624610589}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-235.html', 'title': 'N-235', 'score': 0.9883996928635934}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-384.html', 'title': 'N-384', 'score': 0.9883680344961024}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-709.html', 'title': 'N-709', 'score': 0.9881169227614193}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-692.html', 'title': 'N-692', 'score': 0.9865061946670463}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-300.html', 'title': 'N-300', 'score': 0.9859002674754679}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-117.html', 'title': 'N-117', 'score': 0.9852225983065018}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-33.html', 'title': 'N-33', 'score': 0.9851111321426411}]
result = search.search('lime lime papaya apricot apple tomato peach blueberry',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #415 checking search results for 'lime lime papaya apricot apple tomato peach blueberry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #415 checking search results for 'lime lime papaya apricot apple tomato peach blueberry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #416 checking search results for 'lime kiwi tomato apple banana pear kiwi' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-770.html', 'title': 'N-770', 'score': 0.9999504552318587}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-8.html', 'title': 'N-8', 'score': 0.9998373987407095}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-353.html', 'title': 'N-353', 'score': 0.9979495434913119}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-927.html', 'title': 'N-927', 'score': 0.9971460718028791}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-16.html', 'title': 'N-16', 'score': 0.9961591612452563}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-682.html', 'title': 'N-682', 'score': 0.995930308373878}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-494.html', 'title': 'N-494', 'score': 0.9956449738431232}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-652.html', 'title': 'N-652', 'score': 0.9955428836298519}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-919.html', 'title': 'N-919', 'score': 0.9953486301588614}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-790.html', 'title': 'N-790', 'score': 0.9935022179677514}]
result = search.search('lime kiwi tomato apple banana pear kiwi',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #416 checking search results for 'lime kiwi tomato apple banana pear kiwi' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #416 checking search results for 'lime kiwi tomato apple banana pear kiwi' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #417 checking search results for 'banana blueberry peach blueberry coconut peach apple' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-426.html', 'title': 'N-426', 'score': 0.9998895443160908}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-707.html', 'title': 'N-707', 'score': 0.9967777866928622}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-682.html', 'title': 'N-682', 'score': 0.9955028972081862}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-758.html', 'title': 'N-758', 'score': 0.9949320573149274}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-914.html', 'title': 'N-914', 'score': 0.9948951543096587}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-47.html', 'title': 'N-47', 'score': 0.9933977087740212}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-348.html', 'title': 'N-348', 'score': 0.9931726303562839}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-293.html', 'title': 'N-293', 'score': 0.9927078279952463}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-337.html', 'title': 'N-337', 'score': 0.9925423450534226}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-464.html', 'title': 'N-464', 'score': 0.9924305720433532}]
result = search.search('banana blueberry peach blueberry coconut peach apple',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #417 checking search results for 'banana blueberry peach blueberry coconut peach apple' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #417 checking search results for 'banana blueberry peach blueberry coconut peach apple' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #418 checking search results for 'papaya banana apple lime blueberry' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-96.html', 'title': 'N-96', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-164.html', 'title': 'N-164', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-865.html', 'title': 'N-865', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-484.html', 'title': 'N-484', 'score': 0.99807867083422}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-234.html', 'title': 'N-234', 'score': 0.9978073268136763}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-991.html', 'title': 'N-991', 'score': 0.9968170166349732}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-208.html', 'title': 'N-208', 'score': 0.9964837511994518}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-237.html', 'title': 'N-237', 'score': 0.9954230786262935}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-216.html', 'title': 'N-216', 'score': 0.9949932755542445}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-888.html', 'title': 'N-888', 'score': 0.9949701726873023}]
result = search.search('papaya banana apple lime blueberry',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #418 checking search results for 'papaya banana apple lime blueberry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #418 checking search results for 'papaya banana apple lime blueberry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #419 checking search results for 'peach pear pear papaya kiwi apple papaya' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-789.html', 'title': 'N-789', 'score': 0.9999092816236316}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-200.html', 'title': 'N-200', 'score': 0.9998982256733588}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-684.html', 'title': 'N-684', 'score': 0.99985257589584}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-634.html', 'title': 'N-634', 'score': 0.9963825824386998}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-458.html', 'title': 'N-458', 'score': 0.9905574894549315}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-322.html', 'title': 'N-322', 'score': 0.9872272851876706}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-122.html', 'title': 'N-122', 'score': 0.9871825619827898}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-232.html', 'title': 'N-232', 'score': 0.9867151616246853}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-658.html', 'title': 'N-658', 'score': 0.9863946057546511}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-619.html', 'title': 'N-619', 'score': 0.9863304061807611}]
result = search.search('peach pear pear papaya kiwi apple papaya',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #419 checking search results for 'peach pear pear papaya kiwi apple papaya' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #419 checking search results for 'peach pear pear papaya kiwi apple papaya' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #420 checking search results for 'kiwi lime banana papaya cherry orange blueberry papaya' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-332.html', 'title': 'N-332', 'score': 0.9937539983760331}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-264.html', 'title': 'N-264', 'score': 0.9912499722588096}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-286.html', 'title': 'N-286', 'score': 0.9912350367963327}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-9.html', 'title': 'N-9', 'score': 0.9888742036532723}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-11.html', 'title': 'N-11', 'score': 0.9882381914174847}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-66.html', 'title': 'N-66', 'score': 0.987359892908189}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-757.html', 'title': 'N-757', 'score': 0.9872130892496818}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-964.html', 'title': 'N-964', 'score': 0.9857905291328536}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-63.html', 'title': 'N-63', 'score': 0.9835933402003756}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-672.html', 'title': 'N-672', 'score': 0.9831843620882893}]
result = search.search('kiwi lime banana papaya cherry orange blueberry papaya',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #420 checking search results for 'kiwi lime banana papaya cherry orange blueberry papaya' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #420 checking search results for 'kiwi lime banana papaya cherry orange blueberry papaya' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #421 checking search results for 'pear peach cherry fig peach papaya kiwi lime' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-254.html', 'title': 'N-254', 'score': 0.990628341968062}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-505.html', 'title': 'N-505', 'score': 0.9890447931313412}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-465.html', 'title': 'N-465', 'score': 0.9881342026700195}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-596.html', 'title': 'N-596', 'score': 0.9879587447239475}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-448.html', 'title': 'N-448', 'score': 0.9862456482883387}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-606.html', 'title': 'N-606', 'score': 0.9850312349329912}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-394.html', 'title': 'N-394', 'score': 0.9841720517343493}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-852.html', 'title': 'N-852', 'score': 0.9831121544281061}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-622.html', 'title': 'N-622', 'score': 0.9825355429282321}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-966.html', 'title': 'N-966', 'score': 0.9819391611214364}]
result = search.search('pear peach cherry fig peach papaya kiwi lime',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #421 checking search results for 'pear peach cherry fig peach papaya kiwi lime' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #421 checking search results for 'pear peach cherry fig peach papaya kiwi lime' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #422 checking search results for 'kiwi apricot papaya kiwi orange pear fig fig' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-174.html', 'title': 'N-174', 'score': 0.9943929497338674}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-195.html', 'title': 'N-195', 'score': 0.9940935852772624}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-373.html', 'title': 'N-373', 'score': 0.9925879388364833}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-55.html', 'title': 'N-55', 'score': 0.9901555976872334}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-109.html', 'title': 'N-109', 'score': 0.9890701773367085}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-996.html', 'title': 'N-996', 'score': 0.9890132175821191}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-719.html', 'title': 'N-719', 'score': 0.9889224490829122}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-600.html', 'title': 'N-600', 'score': 0.9863815601365444}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-692.html', 'title': 'N-692', 'score': 0.9848004090865385}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-750.html', 'title': 'N-750', 'score': 0.9832612582560561}]
result = search.search('kiwi apricot papaya kiwi orange pear fig fig',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #422 checking search results for 'kiwi apricot papaya kiwi orange pear fig fig' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #422 checking search results for 'kiwi apricot papaya kiwi orange pear fig fig' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #423 checking search results for 'apricot banana peach papaya coconut' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-219.html', 'title': 'N-219', 'score': 0.9986855702202297}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-234.html', 'title': 'N-234', 'score': 0.9979679690965185}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-210.html', 'title': 'N-210', 'score': 0.9971051828730978}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-495.html', 'title': 'N-495', 'score': 0.9950616280757966}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-917.html', 'title': 'N-917', 'score': 0.9930248518274707}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-574.html', 'title': 'N-574', 'score': 0.9916709162360885}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-542.html', 'title': 'N-542', 'score': 0.9910389870086022}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-725.html', 'title': 'N-725', 'score': 0.9909760377938238}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-813.html', 'title': 'N-813', 'score': 0.990367279348044}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-358.html', 'title': 'N-358', 'score': 0.9903073477977112}]
result = search.search('apricot banana peach papaya coconut',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #423 checking search results for 'apricot banana peach papaya coconut' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #423 checking search results for 'apricot banana peach papaya coconut' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #424 checking search results for 'apricot apple pear banana apricot' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-617.html', 'title': 'N-617', 'score': 0.9997681029630788}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-720.html', 'title': 'N-720', 'score': 0.9997633293244645}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-538.html', 'title': 'N-538', 'score': 0.9997111166679647}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-263.html', 'title': 'N-263', 'score': 0.9995771154443084}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-493.html', 'title': 'N-493', 'score': 0.9993250571902534}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-133.html', 'title': 'N-133', 'score': 0.9989186971731987}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-353.html', 'title': 'N-353', 'score': 0.9978722717463367}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-340.html', 'title': 'N-340', 'score': 0.9975986652318324}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-25.html', 'title': 'N-25', 'score': 0.9968792647846805}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-682.html', 'title': 'N-682', 'score': 0.9965710209144875}]
result = search.search('apricot apple pear banana apricot',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #424 checking search results for 'apricot apple pear banana apricot' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #424 checking search results for 'apricot apple pear banana apricot' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #425 checking search results for 'lime pear coconut lime pear papaya blueberry tomato' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-870.html', 'title': 'N-870', 'score': 0.9914923978659255}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-896.html', 'title': 'N-896', 'score': 0.9912114467410956}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-642.html', 'title': 'N-642', 'score': 0.9909639766530077}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-434.html', 'title': 'N-434', 'score': 0.9890443248334455}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-321.html', 'title': 'N-321', 'score': 0.9885252639234151}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-915.html', 'title': 'N-915', 'score': 0.9877877938273335}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-821.html', 'title': 'N-821', 'score': 0.9875656634093533}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-180.html', 'title': 'N-180', 'score': 0.9870399400129007}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-49.html', 'title': 'N-49', 'score': 0.9851479418693444}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-675.html', 'title': 'N-675', 'score': 0.9850069324753966}]
result = search.search('lime pear coconut lime pear papaya blueberry tomato',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #425 checking search results for 'lime pear coconut lime pear papaya blueberry tomato' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #425 checking search results for 'lime pear coconut lime pear papaya blueberry tomato' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #426 checking search results for 'fig banana tomato cherry fig blueberry papaya coconut' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-854.html', 'title': 'N-854', 'score': 0.9941062175924156}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-37.html', 'title': 'N-37', 'score': 0.993614965760631}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-80.html', 'title': 'N-80', 'score': 0.9908224413374677}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-415.html', 'title': 'N-415', 'score': 0.9900745021848499}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-969.html', 'title': 'N-969', 'score': 0.9865918218409157}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-692.html', 'title': 'N-692', 'score': 0.9862481658129797}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-637.html', 'title': 'N-637', 'score': 0.9848864641390659}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-576.html', 'title': 'N-576', 'score': 0.9846936423425927}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-674.html', 'title': 'N-674', 'score': 0.9843709179522996}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-542.html', 'title': 'N-542', 'score': 0.9842351619788882}]
result = search.search('fig banana tomato cherry fig blueberry papaya coconut',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #426 checking search results for 'fig banana tomato cherry fig blueberry papaya coconut' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #426 checking search results for 'fig banana tomato cherry fig blueberry papaya coconut' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #427 checking search results for 'papaya fig banana fig orange' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-660.html', 'title': 'N-660', 'score': 0.9997194380746914}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-756.html', 'title': 'N-756', 'score': 0.9996334398344692}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-161.html', 'title': 'N-161', 'score': 0.9996245404339373}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-96.html', 'title': 'N-96', 'score': 0.9995998232713181}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-632.html', 'title': 'N-632', 'score': 0.9995848307219656}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-417.html', 'title': 'N-417', 'score': 0.999513784519238}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-576.html', 'title': 'N-576', 'score': 0.999330458291189}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-252.html', 'title': 'N-252', 'score': 0.997821659133448}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-407.html', 'title': 'N-407', 'score': 0.9964731214143968}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-848.html', 'title': 'N-848', 'score': 0.9964203869511528}]
result = search.search('papaya fig banana fig orange',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #427 checking search results for 'papaya fig banana fig orange' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #427 checking search results for 'papaya fig banana fig orange' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #428 checking search results for 'fig cherry pear kiwi tomato fig tomato' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-931.html', 'title': 'N-931', 'score': 0.9998574016423184}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-625.html', 'title': 'N-625', 'score': 0.9998390630904818}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-512.html', 'title': 'N-512', 'score': 0.9998007174316913}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-706.html', 'title': 'N-706', 'score': 0.9997925412382997}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-831.html', 'title': 'N-831', 'score': 0.9997415913618621}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-594.html', 'title': 'N-594', 'score': 0.9986888310489519}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-445.html', 'title': 'N-445', 'score': 0.9976720086281512}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-371.html', 'title': 'N-371', 'score': 0.9975388662811416}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-637.html', 'title': 'N-637', 'score': 0.997322586539137}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-193.html', 'title': 'N-193', 'score': 0.9970541408106512}]
result = search.search('fig cherry pear kiwi tomato fig tomato',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #428 checking search results for 'fig cherry pear kiwi tomato fig tomato' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #428 checking search results for 'fig cherry pear kiwi tomato fig tomato' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #429 checking search results for 'peach coconut apricot lime pear blueberry tomato tomato' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-562.html', 'title': 'N-562', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-440.html', 'title': 'N-440', 'score': 0.9964926812644709}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-94.html', 'title': 'N-94', 'score': 0.9961935959609644}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-234.html', 'title': 'N-234', 'score': 0.9956779076280515}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-256.html', 'title': 'N-256', 'score': 0.995502856081793}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html', 'title': 'N-2', 'score': 0.995328795914974}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-968.html', 'title': 'N-968', 'score': 0.9942592523607507}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-846.html', 'title': 'N-846', 'score': 0.9930115938396156}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-291.html', 'title': 'N-291', 'score': 0.9927164205261857}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-544.html', 'title': 'N-544', 'score': 0.9919923390677349}]
result = search.search('peach coconut apricot lime pear blueberry tomato tomato',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #429 checking search results for 'peach coconut apricot lime pear blueberry tomato tomato' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #429 checking search results for 'peach coconut apricot lime pear blueberry tomato tomato' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #430 checking search results for 'apricot fig banana banana papaya apricot cherry' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-655.html', 'title': 'N-655', 'score': 0.9998984703832672}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-478.html', 'title': 'N-478', 'score': 0.9965243791881822}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-57.html', 'title': 'N-57', 'score': 0.992813296640438}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-976.html', 'title': 'N-976', 'score': 0.9924488548536443}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-629.html', 'title': 'N-629', 'score': 0.9923313315397081}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-15.html', 'title': 'N-15', 'score': 0.9903842986025928}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-891.html', 'title': 'N-891', 'score': 0.9897488647512466}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-921.html', 'title': 'N-921', 'score': 0.9896359313263146}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-21.html', 'title': 'N-21', 'score': 0.9891054030733707}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-42.html', 'title': 'N-42', 'score': 0.9887680980935628}]
result = search.search('apricot fig banana banana papaya apricot cherry',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #430 checking search results for 'apricot fig banana banana papaya apricot cherry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #430 checking search results for 'apricot fig banana banana papaya apricot cherry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #431 checking search results for 'fig pear banana orange cherry' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-717.html', 'title': 'N-717', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-885.html', 'title': 'N-885', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-354.html', 'title': 'N-354', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-383.html', 'title': 'N-383', 'score': 0.9980269869427966}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-286.html', 'title': 'N-286', 'score': 0.997985773512706}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-964.html', 'title': 'N-964', 'score': 0.9974294488851858}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-986.html', 'title': 'N-986', 'score': 0.997283063283793}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-394.html', 'title': 'N-394', 'score': 0.9962186801006272}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-968.html', 'title': 'N-968', 'score': 0.9961902328662814}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-254.html', 'title': 'N-254', 'score': 0.9961783967299599}]
result = search.search('fig pear banana orange cherry',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #431 checking search results for 'fig pear banana orange cherry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #431 checking search results for 'fig pear banana orange cherry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #432 checking search results for 'orange banana blueberry coconut banana blueberry banana peach' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-797.html', 'title': 'N-797', 'score': 0.9963268331163792}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-289.html', 'title': 'N-289', 'score': 0.9928888627721136}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-634.html', 'title': 'N-634', 'score': 0.9907157276599924}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-104.html', 'title': 'N-104', 'score': 0.9906854657971509}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-221.html', 'title': 'N-221', 'score': 0.9883913991386566}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-928.html', 'title': 'N-928', 'score': 0.9883145723471815}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-70.html', 'title': 'N-70', 'score': 0.9860979035916145}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-599.html', 'title': 'N-599', 'score': 0.985888917378165}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-90.html', 'title': 'N-90', 'score': 0.985693178103387}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-592.html', 'title': 'N-592', 'score': 0.985693178103387}]
result = search.search('orange banana blueberry coconut banana blueberry banana peach',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #432 checking search results for 'orange banana blueberry coconut banana blueberry banana peach' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #432 checking search results for 'orange banana blueberry coconut banana blueberry banana peach' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #433 checking search results for 'kiwi peach coconut tomato coconut cherry coconut' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-809.html', 'title': 'N-809', 'score': 0.9995278840299977}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-776.html', 'title': 'N-776', 'score': 0.9993517020822589}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-527.html', 'title': 'N-527', 'score': 0.9992217883439192}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-151.html', 'title': 'N-151', 'score': 0.9944969621079508}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-698.html', 'title': 'N-698', 'score': 0.9942639209211855}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-918.html', 'title': 'N-918', 'score': 0.9938538745322567}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-581.html', 'title': 'N-581', 'score': 0.9932158595053966}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-139.html', 'title': 'N-139', 'score': 0.9911481889584856}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-213.html', 'title': 'N-213', 'score': 0.9908563297485722}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-518.html', 'title': 'N-518', 'score': 0.9907588888263306}]
result = search.search('kiwi peach coconut tomato coconut cherry coconut',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #433 checking search results for 'kiwi peach coconut tomato coconut cherry coconut' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #433 checking search results for 'kiwi peach coconut tomato coconut cherry coconut' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #434 checking search results for 'fig banana coconut fig fig tomato blueberry apple' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-414.html', 'title': 'N-414', 'score': 0.9891173648771842}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-407.html', 'title': 'N-407', 'score': 0.988683828810509}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-74.html', 'title': 'N-74', 'score': 0.9875793724973618}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-969.html', 'title': 'N-969', 'score': 0.9841945612202279}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-411.html', 'title': 'N-411', 'score': 0.9836976927361548}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-674.html', 'title': 'N-674', 'score': 0.9828707126301295}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-504.html', 'title': 'N-504', 'score': 0.9825722253526554}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-29.html', 'title': 'N-29', 'score': 0.9802196697011994}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-260.html', 'title': 'N-260', 'score': 0.9797575267574885}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-462.html', 'title': 'N-462', 'score': 0.9789604645849382}]
result = search.search('fig banana coconut fig fig tomato blueberry apple',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #434 checking search results for 'fig banana coconut fig fig tomato blueberry apple' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #434 checking search results for 'fig banana coconut fig fig tomato blueberry apple' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #435 checking search results for 'tomato apple fig pear coconut pear papaya pear' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-93.html', 'title': 'N-93', 'score': 0.9901929226214952}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-678.html', 'title': 'N-678', 'score': 0.9885334309751004}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-553.html', 'title': 'N-553', 'score': 0.9863886092441715}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-917.html', 'title': 'N-917', 'score': 0.9855803667842673}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-549.html', 'title': 'N-549', 'score': 0.9825365556851294}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-413.html', 'title': 'N-413', 'score': 0.9807302233064992}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-813.html', 'title': 'N-813', 'score': 0.9781710554533368}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-693.html', 'title': 'N-693', 'score': 0.978111500731376}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-707.html', 'title': 'N-707', 'score': 0.9771985253424127}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-938.html', 'title': 'N-938', 'score': 0.974100017858168}]
result = search.search('tomato apple fig pear coconut pear papaya pear',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #435 checking search results for 'tomato apple fig pear coconut pear papaya pear' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #435 checking search results for 'tomato apple fig pear coconut pear papaya pear' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #436 checking search results for 'peach banana lime tomato fig pear' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-735.html', 'title': 'N-735', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-544.html', 'title': 'N-544', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-8.html', 'title': 'N-8', 'score': 0.9999999999999999}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-832.html', 'title': 'N-832', 'score': 0.9963831668660789}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-577.html', 'title': 'N-577', 'score': 0.9962274416432234}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-105.html', 'title': 'N-105', 'score': 0.9961763479951328}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-383.html', 'title': 'N-383', 'score': 0.9959152609113833}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-286.html', 'title': 'N-286', 'score': 0.9958591339073868}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-621.html', 'title': 'N-621', 'score': 0.9950008034530827}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-968.html', 'title': 'N-968', 'score': 0.9949547234089459}]
result = search.search('peach banana lime tomato fig pear',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #436 checking search results for 'peach banana lime tomato fig pear' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #436 checking search results for 'peach banana lime tomato fig pear' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #437 checking search results for 'peach coconut blueberry apricot apple' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-684.html', 'title': 'N-684', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-963.html', 'title': 'N-963', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-553.html', 'title': 'N-553', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-234.html', 'title': 'N-234', 'score': 0.9979644580331024}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-968.html', 'title': 'N-968', 'score': 0.9973398546468526}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-648.html', 'title': 'N-648', 'score': 0.9972781705137443}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html', 'title': 'N-2', 'score': 0.9965570766845876}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-767.html', 'title': 'N-767', 'score': 0.9961533677315708}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-94.html', 'title': 'N-94', 'score': 0.9961315956597103}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-219.html', 'title': 'N-219', 'score': 0.9949612567388846}]
result = search.search('peach coconut blueberry apricot apple',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #437 checking search results for 'peach coconut blueberry apricot apple' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #437 checking search results for 'peach coconut blueberry apricot apple' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #438 checking search results for 'coconut blueberry lime blueberry pear' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-354.html', 'title': 'N-354', 'score': 0.9996985764470543}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-71.html', 'title': 'N-71', 'score': 0.9996836888882911}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-217.html', 'title': 'N-217', 'score': 0.9995195441296479}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-739.html', 'title': 'N-739', 'score': 0.997747588776392}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-509.html', 'title': 'N-509', 'score': 0.9976962462160942}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-226.html', 'title': 'N-226', 'score': 0.9971311209284915}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-682.html', 'title': 'N-682', 'score': 0.9966642430684737}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-353.html', 'title': 'N-353', 'score': 0.9965663465959148}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-559.html', 'title': 'N-559', 'score': 0.996020046683916}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-879.html', 'title': 'N-879', 'score': 0.9959664966894594}]
result = search.search('coconut blueberry lime blueberry pear',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #438 checking search results for 'coconut blueberry lime blueberry pear' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #438 checking search results for 'coconut blueberry lime blueberry pear' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #439 checking search results for 'kiwi peach banana kiwi apricot peach lime apple' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-285.html', 'title': 'N-285', 'score': 0.9963491550521574}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-160.html', 'title': 'N-160', 'score': 0.9956258293190452}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-758.html', 'title': 'N-758', 'score': 0.9950026106020448}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-494.html', 'title': 'N-494', 'score': 0.9897364632308565}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-919.html', 'title': 'N-919', 'score': 0.9877208003310708}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-612.html', 'title': 'N-612', 'score': 0.9876454209078197}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-604.html', 'title': 'N-604', 'score': 0.9875826975792321}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-64.html', 'title': 'N-64', 'score': 0.9864691030614914}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-149.html', 'title': 'N-149', 'score': 0.9854293005866551}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-245.html', 'title': 'N-245', 'score': 0.9854228774528339}]
result = search.search('kiwi peach banana kiwi apricot peach lime apple',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #439 checking search results for 'kiwi peach banana kiwi apricot peach lime apple' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #439 checking search results for 'kiwi peach banana kiwi apricot peach lime apple' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #440 checking search results for 'apple apple coconut orange peach lime lime tomato' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-561.html', 'title': 'N-561', 'score': 0.99995227828019}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-781.html', 'title': 'N-781', 'score': 0.9979863435465767}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-102.html', 'title': 'N-102', 'score': 0.9952609561414745}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-406.html', 'title': 'N-406', 'score': 0.9942947607402888}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-524.html', 'title': 'N-524', 'score': 0.9939747652630886}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-724.html', 'title': 'N-724', 'score': 0.993224560193054}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-70.html', 'title': 'N-70', 'score': 0.9927134543947932}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-635.html', 'title': 'N-635', 'score': 0.9926585476195935}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-969.html', 'title': 'N-969', 'score': 0.9918168517075654}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-450.html', 'title': 'N-450', 'score': 0.9915719474060369}]
result = search.search('apple apple coconut orange peach lime lime tomato',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #440 checking search results for 'apple apple coconut orange peach lime lime tomato' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #440 checking search results for 'apple apple coconut orange peach lime lime tomato' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #441 checking search results for 'orange banana peach kiwi orange' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-212.html', 'title': 'N-212', 'score': 0.9995578494788252}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-621.html', 'title': 'N-621', 'score': 0.9985090214506861}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-25.html', 'title': 'N-25', 'score': 0.9983340178293224}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-976.html', 'title': 'N-976', 'score': 0.9968969598058327}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-890.html', 'title': 'N-890', 'score': 0.9968822804537738}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-698.html', 'title': 'N-698', 'score': 0.996585782210897}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-207.html', 'title': 'N-207', 'score': 0.9965219128726963}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-917.html', 'title': 'N-917', 'score': 0.9965052190166349}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-939.html', 'title': 'N-939', 'score': 0.9959932843017906}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-479.html', 'title': 'N-479', 'score': 0.9952584738169865}]
result = search.search('orange banana peach kiwi orange',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #441 checking search results for 'orange banana peach kiwi orange' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #441 checking search results for 'orange banana peach kiwi orange' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #442 checking search results for 'tomato peach pear blueberry apple cherry banana blueberry' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-439.html', 'title': 'N-439', 'score': 0.9947448881741311}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-711.html', 'title': 'N-711', 'score': 0.9943611553899094}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-226.html', 'title': 'N-226', 'score': 0.9929532076140382}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-148.html', 'title': 'N-148', 'score': 0.9917807034785747}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-719.html', 'title': 'N-719', 'score': 0.9892262055403425}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-614.html', 'title': 'N-614', 'score': 0.9888159472871405}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-464.html', 'title': 'N-464', 'score': 0.9880435617174396}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-529.html', 'title': 'N-529', 'score': 0.9880065595218381}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-784.html', 'title': 'N-784', 'score': 0.9879742089489071}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-597.html', 'title': 'N-597', 'score': 0.9875399899009756}]
result = search.search('tomato peach pear blueberry apple cherry banana blueberry',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #442 checking search results for 'tomato peach pear blueberry apple cherry banana blueberry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #442 checking search results for 'tomato peach pear blueberry apple cherry banana blueberry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #443 checking search results for 'fig apricot coconut apricot banana' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-720.html', 'title': 'N-720', 'score': 0.9997629055437048}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-426.html', 'title': 'N-426', 'score': 0.9996566388331214}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-430.html', 'title': 'N-430', 'score': 0.9981027907249697}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-25.html', 'title': 'N-25', 'score': 0.9968532736042421}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-492.html', 'title': 'N-492', 'score': 0.9965103601731292}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-201.html', 'title': 'N-201', 'score': 0.9961973151414993}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-548.html', 'title': 'N-548', 'score': 0.9955097129179835}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-597.html', 'title': 'N-597', 'score': 0.995019521630997}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-406.html', 'title': 'N-406', 'score': 0.9947260443372261}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-264.html', 'title': 'N-264', 'score': 0.9943229295687979}]
result = search.search('fig apricot coconut apricot banana',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #443 checking search results for 'fig apricot coconut apricot banana' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #443 checking search results for 'fig apricot coconut apricot banana' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #444 checking search results for 'banana blueberry orange cherry pear coconut' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-760.html', 'title': 'N-760', 'score': 0.9973867583953541}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-824.html', 'title': 'N-824', 'score': 0.9964932676063113}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-846.html', 'title': 'N-846', 'score': 0.9957908710960997}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-968.html', 'title': 'N-968', 'score': 0.9952314251015254}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-542.html', 'title': 'N-542', 'score': 0.9943655215190695}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-210.html', 'title': 'N-210', 'score': 0.9939722467977516}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-637.html', 'title': 'N-637', 'score': 0.9938839128274014}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-717.html', 'title': 'N-717', 'score': 0.9938830470056857}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-415.html', 'title': 'N-415', 'score': 0.9935952551871546}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-667.html', 'title': 'N-667', 'score': 0.9932701594022961}]
result = search.search('banana blueberry orange cherry pear coconut',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #444 checking search results for 'banana blueberry orange cherry pear coconut' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #444 checking search results for 'banana blueberry orange cherry pear coconut' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #445 checking search results for 'banana orange apple papaya lime lime pear coconut' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-759.html', 'title': 'N-759', 'score': 0.9938711570064417}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-527.html', 'title': 'N-527', 'score': 0.9937828149728286}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-235.html', 'title': 'N-235', 'score': 0.9935252130486691}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-250.html', 'title': 'N-250', 'score': 0.9875014130977816}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-420.html', 'title': 'N-420', 'score': 0.9865839839208258}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-921.html', 'title': 'N-921', 'score': 0.9860306838403938}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-830.html', 'title': 'N-830', 'score': 0.9849853443890708}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-675.html', 'title': 'N-675', 'score': 0.9846129535872395}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-751.html', 'title': 'N-751', 'score': 0.9843976774291386}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-614.html', 'title': 'N-614', 'score': 0.9832482091245014}]
result = search.search('banana orange apple papaya lime lime pear coconut',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #445 checking search results for 'banana orange apple papaya lime lime pear coconut' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #445 checking search results for 'banana orange apple papaya lime lime pear coconut' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #446 checking search results for 'papaya coconut orange fig coconut apricot' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-77.html', 'title': 'N-77', 'score': 0.9997545945529364}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-76.html', 'title': 'N-76', 'score': 0.9967210329340914}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-33.html', 'title': 'N-33', 'score': 0.9966836216386871}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-259.html', 'title': 'N-259', 'score': 0.9965766932153624}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-213.html', 'title': 'N-213', 'score': 0.9956845426151861}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-277.html', 'title': 'N-277', 'score': 0.9948401283282882}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-87.html', 'title': 'N-87', 'score': 0.9939548622829443}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-872.html', 'title': 'N-872', 'score': 0.9935608904802599}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-448.html', 'title': 'N-448', 'score': 0.9934469238143963}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-315.html', 'title': 'N-315', 'score': 0.9932791649355089}]
result = search.search('papaya coconut orange fig coconut apricot',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #446 checking search results for 'papaya coconut orange fig coconut apricot' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #446 checking search results for 'papaya coconut orange fig coconut apricot' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #447 checking search results for 'lime cherry lime fig kiwi apple banana' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-885.html', 'title': 'N-885', 'score': 0.9999677884993453}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-717.html', 'title': 'N-717', 'score': 0.9971606995535579}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-293.html', 'title': 'N-293', 'score': 0.9942154908793125}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-373.html', 'title': 'N-373', 'score': 0.9935872552425778}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-321.html', 'title': 'N-321', 'score': 0.9932513585769835}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-748.html', 'title': 'N-748', 'score': 0.9932267701562267}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-25.html', 'title': 'N-25', 'score': 0.9918806213184249}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-830.html', 'title': 'N-830', 'score': 0.9909059554766309}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-701.html', 'title': 'N-701', 'score': 0.9908220053041693}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-654.html', 'title': 'N-654', 'score': 0.9907509438599804}]
result = search.search('lime cherry lime fig kiwi apple banana',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #447 checking search results for 'lime cherry lime fig kiwi apple banana' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #447 checking search results for 'lime cherry lime fig kiwi apple banana' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #448 checking search results for 'peach apple lime cherry banana' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-413.html', 'title': 'N-413', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-18.html', 'title': 'N-18', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-770.html', 'title': 'N-770', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-672.html', 'title': 'N-672', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-810.html', 'title': 'N-810', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-8.html', 'title': 'N-8', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-617.html', 'title': 'N-617', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-296.html', 'title': 'N-296', 'score': 0.9988328459047211}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-941.html', 'title': 'N-941', 'score': 0.998065755286494}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-230.html', 'title': 'N-230', 'score': 0.9978698385448912}]
result = search.search('peach apple lime cherry banana',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #448 checking search results for 'peach apple lime cherry banana' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #448 checking search results for 'peach apple lime cherry banana' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #449 checking search results for 'cherry banana pear banana blueberry banana blueberry orange' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-873.html', 'title': 'N-873', 'score': 0.9932566299150516}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-104.html', 'title': 'N-104', 'score': 0.9931137575048541}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-336.html', 'title': 'N-336', 'score': 0.9905453363181832}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-153.html', 'title': 'N-153', 'score': 0.9898204328278359}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-174.html', 'title': 'N-174', 'score': 0.9889296597851336}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-368.html', 'title': 'N-368', 'score': 0.9884505333931933}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-928.html', 'title': 'N-928', 'score': 0.9882524535073479}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-221.html', 'title': 'N-221', 'score': 0.9880968540521476}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-42.html', 'title': 'N-42', 'score': 0.9863715036010207}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-237.html', 'title': 'N-237', 'score': 0.9856650136958677}]
result = search.search('cherry banana pear banana blueberry banana blueberry orange',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #449 checking search results for 'cherry banana pear banana blueberry banana blueberry orange' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #449 checking search results for 'cherry banana pear banana blueberry banana blueberry orange' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #450 checking search results for 'banana orange coconut banana pear peach' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-540.html', 'title': 'N-540', 'score': 0.9997669844590791}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-891.html', 'title': 'N-891', 'score': 0.997921254440868}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-273.html', 'title': 'N-273', 'score': 0.9972072938114956}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-879.html', 'title': 'N-879', 'score': 0.9954469740713205}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-195.html', 'title': 'N-195', 'score': 0.9950534413516107}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-24.html', 'title': 'N-24', 'score': 0.994495786480466}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-70.html', 'title': 'N-70', 'score': 0.9935583227341493}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-876.html', 'title': 'N-876', 'score': 0.9929192264713065}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-371.html', 'title': 'N-371', 'score': 0.9910224455945201}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-739.html', 'title': 'N-739', 'score': 0.9909409132876019}]
result = search.search('banana orange coconut banana pear peach',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #450 checking search results for 'banana orange coconut banana pear peach' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #450 checking search results for 'banana orange coconut banana pear peach' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #451 checking search results for 'fig blueberry fig coconut coconut papaya blueberry kiwi' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-252.html', 'title': 'N-252', 'score': 0.9939310685073124}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-51.html', 'title': 'N-51', 'score': 0.9917357722322115}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-148.html', 'title': 'N-148', 'score': 0.9900799917138403}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-419.html', 'title': 'N-419', 'score': 0.9888672194692338}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-580.html', 'title': 'N-580', 'score': 0.9887927399007846}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-262.html', 'title': 'N-262', 'score': 0.988690958815042}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-176.html', 'title': 'N-176', 'score': 0.9865676997305397}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-796.html', 'title': 'N-796', 'score': 0.986094661915391}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-880.html', 'title': 'N-880', 'score': 0.9860237079324363}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-336.html', 'title': 'N-336', 'score': 0.9859096747004842}]
result = search.search('fig blueberry fig coconut coconut papaya blueberry kiwi',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #451 checking search results for 'fig blueberry fig coconut coconut papaya blueberry kiwi' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #451 checking search results for 'fig blueberry fig coconut coconut papaya blueberry kiwi' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #452 checking search results for 'orange fig apricot lime fig blueberry lime apple' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-931.html', 'title': 'N-931', 'score': 0.99074191232218}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-434.html', 'title': 'N-434', 'score': 0.9895191503265071}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-692.html', 'title': 'N-692', 'score': 0.9884619775306269}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-593.html', 'title': 'N-593', 'score': 0.9884072491556772}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-750.html', 'title': 'N-750', 'score': 0.9870968569939541}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-834.html', 'title': 'N-834', 'score': 0.9863103035464257}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-142.html', 'title': 'N-142', 'score': 0.9857662106614506}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-600.html', 'title': 'N-600', 'score': 0.983334914480372}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-969.html', 'title': 'N-969', 'score': 0.9819233721332736}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-403.html', 'title': 'N-403', 'score': 0.981570323228615}]
result = search.search('orange fig apricot lime fig blueberry lime apple',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #452 checking search results for 'orange fig apricot lime fig blueberry lime apple' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #452 checking search results for 'orange fig apricot lime fig blueberry lime apple' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #453 checking search results for 'fig kiwi pear cherry kiwi banana' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-8.html', 'title': 'N-8', 'score': 0.999752324447462}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-199.html', 'title': 'N-199', 'score': 0.9978484343142486}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-493.html', 'title': 'N-493', 'score': 0.997619352795166}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-203.html', 'title': 'N-203', 'score': 0.9962820168591883}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-463.html', 'title': 'N-463', 'score': 0.995835793241565}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-149.html', 'title': 'N-149', 'score': 0.9951626354714056}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-384.html', 'title': 'N-384', 'score': 0.9951432746624232}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-927.html', 'title': 'N-927', 'score': 0.9950199767828073}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-596.html', 'title': 'N-596', 'score': 0.9933325490761152}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-652.html', 'title': 'N-652', 'score': 0.9931138416237508}]
result = search.search('fig kiwi pear cherry kiwi banana',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #453 checking search results for 'fig kiwi pear cherry kiwi banana' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #453 checking search results for 'fig kiwi pear cherry kiwi banana' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #454 checking search results for 'coconut fig kiwi blueberry lime cherry kiwi' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-891.html', 'title': 'N-891', 'score': 0.9895827820902501}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-652.html', 'title': 'N-652', 'score': 0.9885207679956689}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-149.html', 'title': 'N-149', 'score': 0.9868918249777061}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-927.html', 'title': 'N-927', 'score': 0.9867403940709084}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-542.html', 'title': 'N-542', 'score': 0.9866465039245694}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-43.html', 'title': 'N-43', 'score': 0.9863282205194795}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-562.html', 'title': 'N-562', 'score': 0.9858681877530535}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-352.html', 'title': 'N-352', 'score': 0.9858205862293022}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-863.html', 'title': 'N-863', 'score': 0.9853706727883089}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-493.html', 'title': 'N-493', 'score': 0.9852799709961111}]
result = search.search('coconut fig kiwi blueberry lime cherry kiwi',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #454 checking search results for 'coconut fig kiwi blueberry lime cherry kiwi' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #454 checking search results for 'coconut fig kiwi blueberry lime cherry kiwi' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #455 checking search results for 'tomato lime apple kiwi fig lime' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-885.html', 'title': 'N-885', 'score': 0.9999241216678129}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-373.html', 'title': 'N-373', 'score': 0.9998942766977477}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-584.html', 'title': 'N-584', 'score': 0.9997830962232996}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-942.html', 'title': 'N-942', 'score': 0.9997541273983956}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-748.html', 'title': 'N-748', 'score': 0.9989170522554399}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-68.html', 'title': 'N-68', 'score': 0.998489971450941}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-900.html', 'title': 'N-900', 'score': 0.998456978879213}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-717.html', 'title': 'N-717', 'score': 0.9976325477688284}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-158.html', 'title': 'N-158', 'score': 0.9975010961231414}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-321.html', 'title': 'N-321', 'score': 0.99544876470812}]
result = search.search('tomato lime apple kiwi fig lime',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #455 checking search results for 'tomato lime apple kiwi fig lime' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #455 checking search results for 'tomato lime apple kiwi fig lime' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #456 checking search results for 'cherry lime orange coconut banana orange apple' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-769.html', 'title': 'N-769', 'score': 0.9934456228677676}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-623.html', 'title': 'N-623', 'score': 0.993161274115135}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-439.html', 'title': 'N-439', 'score': 0.9926088299347474}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-234.html', 'title': 'N-234', 'score': 0.9911774944108219}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-145.html', 'title': 'N-145', 'score': 0.990970095963755}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-597.html', 'title': 'N-597', 'score': 0.9908471876330739}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-672.html', 'title': 'N-672', 'score': 0.9902495699415128}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-682.html', 'title': 'N-682', 'score': 0.9895839648179089}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-935.html', 'title': 'N-935', 'score': 0.9895614524899385}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-903.html', 'title': 'N-903', 'score': 0.9884445763107738}]
result = search.search('cherry lime orange coconut banana orange apple',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #456 checking search results for 'cherry lime orange coconut banana orange apple' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #456 checking search results for 'cherry lime orange coconut banana orange apple' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #457 checking search results for 'peach orange orange apple orange blueberry' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-203.html', 'title': 'N-203', 'score': 0.9993388831072001}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-963.html', 'title': 'N-963', 'score': 0.9980177122899034}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-976.html', 'title': 'N-976', 'score': 0.9956274701146316}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-984.html', 'title': 'N-984', 'score': 0.9952533836712397}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-224.html', 'title': 'N-224', 'score': 0.9942085939565212}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-961.html', 'title': 'N-961', 'score': 0.9928937657608322}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-525.html', 'title': 'N-525', 'score': 0.9918842678485775}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-400.html', 'title': 'N-400', 'score': 0.9914321980437815}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-677.html', 'title': 'N-677', 'score': 0.9913040558193339}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-280.html', 'title': 'N-280', 'score': 0.9911256008972192}]
result = search.search('peach orange orange apple orange blueberry',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #457 checking search results for 'peach orange orange apple orange blueberry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #457 checking search results for 'peach orange orange apple orange blueberry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #458 checking search results for 'blueberry peach lime tomato pear blueberry pear papaya' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-457.html', 'title': 'N-457', 'score': 0.997599485480895}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-176.html', 'title': 'N-176', 'score': 0.9959378311478384}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-377.html', 'title': 'N-377', 'score': 0.9955787776948805}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-478.html', 'title': 'N-478', 'score': 0.9951534724295872}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-355.html', 'title': 'N-355', 'score': 0.9943928851948665}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-317.html', 'title': 'N-317', 'score': 0.9929888053916693}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-496.html', 'title': 'N-496', 'score': 0.9916645510685893}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-104.html', 'title': 'N-104', 'score': 0.9907271866116021}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-535.html', 'title': 'N-535', 'score': 0.9893590361496656}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-764.html', 'title': 'N-764', 'score': 0.9879327619794609}]
result = search.search('blueberry peach lime tomato pear blueberry pear papaya',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #458 checking search results for 'blueberry peach lime tomato pear blueberry pear papaya' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #458 checking search results for 'blueberry peach lime tomato pear blueberry pear papaya' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


output.close()
success_output.close()







output.close()
success_output.close()
