
import testingtools
import crawler
import searchdata
import search

#Performing crawl starting at seed http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html
crawler.crawl('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html')


output = open('fruits4-all-outgoing-failed.txt', 'w')
success_output = open('fruits4-all-outgoing-passed.txt', 'w')

#Test #0 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-159.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-852.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-15.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-56.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-159.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #0 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-159.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #0 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-159.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #1 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-792.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-726.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-792.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #1 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-792.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #1 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-792.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #2 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-896.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-143.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-901.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-896.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #2 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-896.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #2 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-896.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #3 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-110.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-59.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-73.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-110.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #3 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-110.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #3 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-110.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #4 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-385.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-338.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-823.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-169.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-385.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #4 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-385.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #4 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-385.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #5 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-450.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-323.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-529.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-596.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-756.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-929.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-450.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #5 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-450.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #5 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-450.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #6 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-501.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-121.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-295.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-456.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-795.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-889.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-501.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #6 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-501.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #6 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-501.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #7 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-391.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-14.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-391.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #7 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-391.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #7 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-391.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #8 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-740.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-12.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-362.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-740.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #8 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-740.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #8 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-740.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #9 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-28.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-41.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-89.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-16.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-142.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-334.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-353.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-375.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-947.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-28.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #9 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-28.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #9 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-28.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #10 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-478.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-921.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-231.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-478.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #10 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-478.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #10 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-478.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #11 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-140.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-121.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-222.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-453.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-874.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-140.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #11 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-140.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #11 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-140.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #12 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-21.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-98.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-102.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-323.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-799.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-81.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-156.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-21.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #12 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-21.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #12 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-21.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #13 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-668.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-640.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-668.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #13 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-668.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #13 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-668.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #14 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-788.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-326.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-943.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-788.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #14 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-788.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #14 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-788.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #15 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-867.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-867.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #15 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-867.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #15 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-867.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #16 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-388.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-8.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-103.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-388.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #16 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-388.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #16 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-388.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #17 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-497.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-80.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-497.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #17 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-497.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #17 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-497.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #18 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-52.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-817.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-8.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-602.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-52.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #18 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-52.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #18 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-52.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #19 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-511.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-102.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-700.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-511.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #19 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-511.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #19 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-511.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #20 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-83.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-427.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-83.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #20 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-83.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #20 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-83.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #21 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-786.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-18.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-786.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #21 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-786.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #21 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-786.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #22 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-447.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-253.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-820.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-447.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #22 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-447.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #22 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-447.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #23 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-134.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-8.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-33.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-134.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #23 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-134.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #23 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-134.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #24 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-84.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-22.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-61.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-251.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-382.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-488.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-84.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #24 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-84.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #24 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-84.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #25 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-226.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-54.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-226.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #25 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-226.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #25 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-226.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #26 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-620.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-49.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-620.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #26 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-620.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #26 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-620.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #27 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-557.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-269.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-557.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #27 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-557.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #27 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-557.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #28 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-884.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-299.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-445.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-884.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #28 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-884.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #28 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-884.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #29 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-283.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-238.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-290.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-283.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #29 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-283.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #29 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-283.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #30 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-709.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-709.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #30 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-709.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #30 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-709.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #31 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-606.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-452.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-733.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-826.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-606.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #31 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-606.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #31 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-606.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #32 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-27.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-12.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-27.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #32 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-27.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #32 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-27.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #33 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-10.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-9.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-173.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-576.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-32.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-75.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-177.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-10.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #33 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-10.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #33 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-10.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #34 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-339.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-307.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-425.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-375.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-339.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #34 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-339.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #34 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-339.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #35 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-989.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-54.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-874.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-213.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-622.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-989.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #35 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-989.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #35 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-989.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #36 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-755.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-618.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-755.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #36 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-755.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #36 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-755.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #37 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-749.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-292.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-382.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-6.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-749.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #37 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-749.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #37 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-749.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #38 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-728.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-330.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-380.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-728.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #38 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-728.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #38 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-728.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #39 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-430.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-411.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-343.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-488.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-430.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #39 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-430.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #39 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-430.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #40 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-527.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-527.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #40 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-527.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #40 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-527.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #41 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-157.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-149.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-157.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #41 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-157.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #41 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-157.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #42 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-997.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-23.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-997.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #42 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-997.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #42 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-997.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #43 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-419.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-144.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-419.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #43 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-419.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #43 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-419.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #44 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-48.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-14.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-50.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-70.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-131.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-145.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-444.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-645.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-167.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-324.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-554.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-48.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #44 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-48.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #44 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-48.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #45 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-199.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-43.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-881.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-199.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #45 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-199.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #45 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-199.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #46 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-479.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-190.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-781.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-479.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #46 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-479.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #46 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-479.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #47 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-313.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-43.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-313.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #47 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-313.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #47 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-313.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #48 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-932.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-105.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-932.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #48 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-932.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #48 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-932.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #49 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-286.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-113.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-347.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-561.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-568.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-315.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-813.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-286.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #49 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-286.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #49 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-286.html\n\n')
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









output = open('fruits4-all-incoming-failed.txt', 'w')
success_output = open('fruits4-all-incoming-passed.txt', 'w')

#Test #51 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-662.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-662.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #51 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-662.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #51 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-662.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #52 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-743.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-54.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-779.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-716.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-743.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #52 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-743.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #52 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-743.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #53 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-304.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-9.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-151.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-604.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-946.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-349.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-451.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-848.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-304.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #53 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-304.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #53 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-304.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #54 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-404.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-56.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-404.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #54 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-404.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #54 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-404.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #55 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-518.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-92.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-518.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #55 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-518.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #55 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-518.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #56 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-204.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-169.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-108.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-774.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-204.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #56 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-204.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #56 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-204.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #57 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-64.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-179.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-14.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-267.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-934.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-253.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-470.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-747.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-895.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-125.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-454.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-604.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-806.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-64.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #57 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-64.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #57 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-64.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #58 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-400.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-79.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-400.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #58 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-400.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #58 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-400.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #59 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-209.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-7.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-280.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-281.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-383.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-209.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #59 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-209.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #59 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-209.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #60 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-824.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-785.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-824.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #60 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-824.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #60 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-824.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #61 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-492.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-389.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-492.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #61 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-492.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #61 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-492.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #62 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-268.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-4.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-467.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-227.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-344.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-875.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-268.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #62 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-268.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #62 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-268.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #63 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-753.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-56.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-753.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #63 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-753.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #63 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-753.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #64 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-705.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-23.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-705.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #64 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-705.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #64 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-705.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #65 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-596.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-178.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-252.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-952.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-450.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-735.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-942.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-596.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #65 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-596.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #65 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-596.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #66 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-447.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-253.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-820.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-447.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #66 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-447.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #66 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-447.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #67 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-838.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-290.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-838.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #67 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-838.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #67 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-838.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #68 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-822.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-12.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-822.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #68 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-822.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #68 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-822.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #69 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-741.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-95.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-830.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-741.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #69 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-741.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #69 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-741.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #70 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-834.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-143.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-257.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-834.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #70 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-834.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #70 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-834.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #71 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-674.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-674.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #71 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-674.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #71 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-674.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #72 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-183.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-218.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-41.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-658.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-183.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #72 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-183.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #72 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-183.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #73 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-936.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-61.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-936.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #73 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-936.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #73 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-936.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #74 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-542.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-342.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-542.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #74 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-542.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #74 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-542.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #75 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-122.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-574.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-122.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #75 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-122.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #75 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-122.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #76 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-898.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-9.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-898.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #76 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-898.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #76 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-898.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #77 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-289.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-43.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-305.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-289.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #77 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-289.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #77 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-289.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #78 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-303.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-151.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-303.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #78 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-303.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #78 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-303.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #79 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-114.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-12.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-114.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #79 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-114.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #79 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-114.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #80 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-245.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-120.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-245.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #80 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-245.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #80 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-245.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #81 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-672.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-279.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-672.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #81 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-672.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #81 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-672.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #82 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-47.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-62.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-47.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #82 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-47.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #82 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-47.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #83 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-862.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-15.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-597.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-862.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #83 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-862.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #83 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-862.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #84 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-315.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-286.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-11.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-693.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-80.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-315.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #84 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-315.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #84 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-315.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #85 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-352.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-7.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-96.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-196.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-352.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #85 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-352.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #85 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-352.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #86 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-410.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-8.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-70.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-410.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #86 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-410.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #86 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-410.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #87 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-211.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-103.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-211.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #87 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-211.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #87 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-211.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #88 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-69.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-12.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-113.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-76.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-262.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-100.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-133.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-715.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-885.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-69.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #88 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-69.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #88 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-69.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #89 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-463.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-4.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-463.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #89 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-463.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #89 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-463.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #90 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-554.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-48.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-554.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #90 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-554.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #90 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-554.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #91 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-12.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-45.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-757.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-9.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-37.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-40.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-70.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-75.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-101.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-114.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-147.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-155.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-224.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-235.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-251.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-319.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-338.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-377.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-440.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-486.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-493.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-500.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-513.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-516.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-538.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-567.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-621.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-638.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-643.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-681.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-740.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-807.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-821.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-841.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-5.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-15.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-27.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-30.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-43.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-69.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-72.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-89.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-115.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-178.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-179.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-186.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-200.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-279.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-296.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-314.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-333.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-466.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-512.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-519.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-530.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-583.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-614.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-680.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-721.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-736.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-799.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-822.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-870.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-923.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-964.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-12.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #91 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-12.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #91 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-12.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #92 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-140.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-453.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-121.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-222.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-874.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-140.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #92 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-140.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #92 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-140.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #93 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-157.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-149.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-157.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #93 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-157.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #93 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-157.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #94 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-11.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-315.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-151.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-59.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-949.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-287.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-51.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-694.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-171.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-193.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-234.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-650.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-11.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #94 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-11.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #94 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-11.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #95 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-104.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-7.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-541.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-446.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-80.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-256.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-563.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-112.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-104.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #95 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-104.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #95 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-104.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #96 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-986.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-643.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-986.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #96 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-986.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #96 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-986.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #97 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-998.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-717.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-998.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #97 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-998.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #97 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-998.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #98 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-255.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-255.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #98 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-255.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #98 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-255.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #99 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-283.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-238.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-290.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-283.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #99 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-283.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #99 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-283.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #100 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-418.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-418.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #100 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-418.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #100 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-418.html\n\n')
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









output = open('fruits4-all-pagerank-failed.txt', 'w')
success_output = open('fruits4-all-pagerank-passed.txt', 'w')

#Test #102 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-626.html
expected = 0.000369644439687086
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-626.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #102 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-626.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #102 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-626.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #103 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-456.html
expected = 0.0008887731564580115
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-456.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #103 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-456.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #103 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-456.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #104 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-907.html
expected = 0.0009329031322563916
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-907.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #104 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-907.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #104 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-907.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #105 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-191.html
expected = 0.0012989080171989026
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-191.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #105 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-191.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #105 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-191.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #106 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-779.html
expected = 0.00041123791572535016
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-779.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #106 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-779.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #106 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-779.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #107 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-775.html
expected = 0.0004782511341167684
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-775.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #107 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-775.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #107 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-775.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #108 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-658.html
expected = 0.0006423167275483628
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-658.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #108 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-658.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #108 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-658.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #109 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-768.html
expected = 0.0006182258022204698
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-768.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #109 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-768.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #109 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-768.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #110 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-746.html
expected = 0.0003976133403082597
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-746.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #110 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-746.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #110 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-746.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #111 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-433.html
expected = 0.0012490434665047637
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-433.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #111 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-433.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #111 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-433.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #112 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-471.html
expected = 0.0006862763655490483
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-471.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #112 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-471.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #112 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-471.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #113 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-594.html
expected = 0.00035377166889291053
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-594.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #113 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-594.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #113 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-594.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #114 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-925.html
expected = 0.0004096034208182203
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-925.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #114 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-925.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #114 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-925.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #115 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-257.html
expected = 0.001543155259441255
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-257.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #115 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-257.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #115 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-257.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #116 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-586.html
expected = 0.000634231417807155
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-586.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #116 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-586.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #116 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-586.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #117 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-209.html
expected = 0.0014573155912372502
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-209.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #117 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-209.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #117 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-209.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #118 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-765.html
expected = 0.0010270691789534053
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-765.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #118 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-765.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #118 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-765.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #119 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-602.html
expected = 0.0004530261851872726
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-602.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #119 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-602.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #119 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-602.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #120 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-92.html
expected = 0.002426074171474621
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-92.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #120 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-92.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #120 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-92.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #121 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-528.html
expected = 0.00039162029527686624
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-528.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #121 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-528.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #121 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-528.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #122 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-993.html
expected = 0.0003707731661078087
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-993.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #122 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-993.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #122 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-993.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #123 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-863.html
expected = 0.0003865749163329739
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-863.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #123 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-863.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #123 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-863.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #124 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-283.html
expected = 0.0009532810917749505
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-283.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #124 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-283.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #124 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-283.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #125 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-129.html
expected = 0.0014274462990001623
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-129.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #125 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-129.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #125 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-129.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #126 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-895.html
expected = 0.0003830469786999205
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-895.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #126 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-895.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #126 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-895.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #127 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-980.html
expected = 0.0006841205719719826
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-980.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #127 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-980.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #127 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-980.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #128 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-976.html
expected = 0.0006664452478245812
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-976.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #128 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-976.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #128 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-976.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #129 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-339.html
expected = 0.0010776649943209894
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-339.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #129 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-339.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #129 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-339.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #130 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-483.html
expected = 0.00035898075656200283
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-483.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #130 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-483.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #130 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-483.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #131 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-699.html
expected = 0.0006488509392697962
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-699.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #131 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-699.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #131 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-699.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #132 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-256.html
expected = 0.0017292788162939791
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-256.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #132 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-256.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #132 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-256.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #133 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-113.html
expected = 0.0022924375917572713
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-113.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #133 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-113.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #133 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-113.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #134 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-756.html
expected = 0.0006298503677811337
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-756.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #134 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-756.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #134 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-756.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #135 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-539.html
expected = 0.0006951605298371361
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-539.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #135 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-539.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #135 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-539.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #136 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-440.html
expected = 0.0008916968898745633
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-440.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #136 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-440.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #136 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-440.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #137 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-212.html
expected = 0.000649624353170853
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-212.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #137 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-212.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #137 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-212.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #138 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-591.html
expected = 0.00038662698738077815
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-591.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #138 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-591.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #138 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-591.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #139 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-622.html
expected = 0.001391236699250788
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-622.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #139 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-622.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #139 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-622.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #140 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-888.html
expected = 0.00036492920035369967
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-888.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #140 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-888.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #140 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-888.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #141 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-724.html
expected = 0.0011938084974471325
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-724.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #141 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-724.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #141 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-724.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #142 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-743.html
expected = 0.0010352965243047901
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-743.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #142 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-743.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #142 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-743.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #143 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-650.html
expected = 0.00037339721343381964
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-650.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #143 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-650.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #143 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-650.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #144 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-293.html
expected = 0.00036374895584914316
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-293.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #144 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-293.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #144 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-293.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #145 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-530.html
expected = 0.0006454132647425771
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-530.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #145 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-530.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #145 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-530.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #146 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-294.html
expected = 0.0003627824664744897
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-294.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #146 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-294.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #146 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-294.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #147 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-647.html
expected = 0.0006348464039542202
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-647.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #147 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-647.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #147 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-647.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #148 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-720.html
expected = 0.0003616007736401716
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-720.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #148 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-720.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #148 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-720.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #149 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-176.html
expected = 0.00042479315601873176
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-176.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #149 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-176.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #149 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-176.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #150 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-549.html
expected = 0.0004515875011094794
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-549.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #150 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-549.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #150 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-549.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #151 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-228.html
expected = 0.0006722738437113984
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-228.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #151 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-228.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #151 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-228.html\n\n')
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









output = open('fruits4-all-idf-failed.txt', 'w')
success_output = open('fruits4-all-idf-passed.txt', 'w')

#Test #153 checking IDF for word papaya
expected = 0.16974467583231712
result = searchdata.get_idf('papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #153 checking IDF for word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #153 checking IDF for word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #154 checking IDF for word pear
expected = 0.17462139610706884
result = searchdata.get_idf('pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #154 checking IDF for word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #154 checking IDF for word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #155 checking IDF for word orange
expected = 0.17136841831198113
result = searchdata.get_idf('orange')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #155 checking IDF for word orange\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #155 checking IDF for word orange\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #156 checking IDF for word fig
expected = 0.17462139610706884
result = searchdata.get_idf('fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #156 checking IDF for word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #156 checking IDF for word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #157 checking IDF for word banana
expected = 0.16650266314016507
result = searchdata.get_idf('banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #157 checking IDF for word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #157 checking IDF for word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #158 checking IDF for word cherry
expected = 0.18114943910456646
result = searchdata.get_idf('cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #158 checking IDF for word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #158 checking IDF for word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #159 checking IDF for word lime
expected = 0.18278607574167338
result = searchdata.get_idf('lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #159 checking IDF for word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #159 checking IDF for word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #160 checking IDF for word apple
expected = 0.18114943910456646
result = searchdata.get_idf('apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #160 checking IDF for word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #160 checking IDF for word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #161 checking IDF for word blueberry
expected = 0.17136841831198113
result = searchdata.get_idf('blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #161 checking IDF for word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #161 checking IDF for word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #162 checking IDF for word kiwi
expected = 0.1729939903610231
result = searchdata.get_idf('kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #162 checking IDF for word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #162 checking IDF for word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #163 checking IDF for word apricot
expected = 0.14560532224689926
result = searchdata.get_idf('apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #163 checking IDF for word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #163 checking IDF for word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #164 checking IDF for word coconut
expected = 0.18114943910456646
result = searchdata.get_idf('coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #164 checking IDF for word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #164 checking IDF for word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #165 checking IDF for word peach
expected = 0.1795146570136211
result = searchdata.get_idf('peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #165 checking IDF for word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #165 checking IDF for word peach\n\n')
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









output = open('fruits4-all-tf-failed.txt', 'w')
success_output = open('fruits4-all-tf-passed.txt', 'w')

#Test #167 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-614.html and word pear
expected = 0.08333333333333333
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-614.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #167 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-614.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #167 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-614.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #168 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-614.html and word apricot
expected = 0.09722222222222222
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-614.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #168 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-614.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #168 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-614.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #169 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-614.html and word kiwi
expected = 0.06944444444444445
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-614.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #169 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-614.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #169 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-614.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #170 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-614.html and word cherry
expected = 0.06944444444444445
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-614.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #170 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-614.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #170 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-614.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #171 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-614.html and word peach
expected = 0.05555555555555555
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-614.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #171 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-614.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #171 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-614.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #172 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-614.html and word lime
expected = 0.08333333333333333
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-614.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #172 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-614.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #172 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-614.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #173 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-614.html and word banana
expected = 0.08333333333333333
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-614.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #173 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-614.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #173 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-614.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #174 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-614.html and word papaya
expected = 0.08333333333333333
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-614.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #174 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-614.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #174 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-614.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #175 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-614.html and word blueberry
expected = 0.06944444444444445
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-614.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #175 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-614.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #175 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-614.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #176 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-614.html and word fig
expected = 0.041666666666666664
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-614.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #176 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-614.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #176 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-614.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #177 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-614.html and word tomato
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-614.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #177 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-614.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #177 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-614.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #178 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-873.html and word pear
expected = 0.25
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-873.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #178 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-873.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #178 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-873.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #179 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-873.html and word apricot
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-873.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #179 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-873.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #179 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-873.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #180 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-873.html and word kiwi
expected = 0.0625
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-873.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #180 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-873.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #180 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-873.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #181 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-873.html and word cherry
expected = 0.0625
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-873.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #181 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-873.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #181 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-873.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #182 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-873.html and word peach
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-873.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #182 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-873.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #182 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-873.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #183 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-873.html and word lime
expected = 0.0625
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-873.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #183 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-873.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #183 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-873.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #184 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-873.html and word banana
expected = 0.0625
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-873.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #184 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-873.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #184 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-873.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #185 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-873.html and word papaya
expected = 0.125
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-873.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #185 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-873.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #185 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-873.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #186 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-873.html and word blueberry
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-873.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #186 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-873.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #186 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-873.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #187 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-873.html and word fig
expected = 0.125
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-873.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #187 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-873.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #187 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-873.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #188 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-873.html and word tomato
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-873.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #188 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-873.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #188 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-873.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #189 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-869.html and word pear
expected = 0.08064516129032258
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-869.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #189 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-869.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #189 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-869.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #190 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-869.html and word apricot
expected = 0.0967741935483871
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-869.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #190 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-869.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #190 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-869.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #191 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-869.html and word kiwi
expected = 0.03225806451612903
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-869.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #191 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-869.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #191 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-869.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #192 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-869.html and word cherry
expected = 0.06451612903225806
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-869.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #192 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-869.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #192 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-869.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #193 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-869.html and word peach
expected = 0.04838709677419355
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-869.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #193 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-869.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #193 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-869.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #194 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-869.html and word lime
expected = 0.016129032258064516
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-869.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #194 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-869.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #194 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-869.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #195 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-869.html and word banana
expected = 0.11290322580645161
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-869.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #195 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-869.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #195 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-869.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #196 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-869.html and word papaya
expected = 0.16129032258064516
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-869.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #196 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-869.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #196 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-869.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #197 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-869.html and word blueberry
expected = 0.04838709677419355
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-869.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #197 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-869.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #197 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-869.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #198 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-869.html and word fig
expected = 0.0967741935483871
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-869.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #198 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-869.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #198 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-869.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #199 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-869.html and word tomato
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-869.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #199 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-869.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #199 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-869.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #200 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-815.html and word pear
expected = 0.06521739130434782
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-815.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #200 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-815.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #200 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-815.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #201 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-815.html and word apricot
expected = 0.043478260869565216
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-815.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #201 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-815.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #201 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-815.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #202 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-815.html and word kiwi
expected = 0.10869565217391304
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-815.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #202 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-815.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #202 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-815.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #203 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-815.html and word cherry
expected = 0.021739130434782608
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-815.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #203 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-815.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #203 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-815.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #204 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-815.html and word peach
expected = 0.08695652173913043
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-815.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #204 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-815.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #204 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-815.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #205 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-815.html and word lime
expected = 0.06521739130434782
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-815.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #205 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-815.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #205 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-815.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #206 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-815.html and word banana
expected = 0.06521739130434782
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-815.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #206 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-815.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #206 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-815.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #207 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-815.html and word papaya
expected = 0.10869565217391304
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-815.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #207 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-815.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #207 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-815.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #208 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-815.html and word blueberry
expected = 0.15217391304347827
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-815.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #208 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-815.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #208 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-815.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #209 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-815.html and word fig
expected = 0.06521739130434782
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-815.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #209 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-815.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #209 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-815.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #210 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-815.html and word tomato
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-815.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #210 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-815.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #210 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-815.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #211 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-535.html and word pear
expected = 0.025
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-535.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #211 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-535.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #211 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-535.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #212 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-535.html and word apricot
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-535.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #212 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-535.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #212 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-535.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #213 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-535.html and word kiwi
expected = 0.15
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-535.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #213 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-535.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #213 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-535.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #214 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-535.html and word cherry
expected = 0.125
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-535.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #214 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-535.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #214 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-535.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #215 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-535.html and word peach
expected = 0.075
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-535.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #215 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-535.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #215 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-535.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #216 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-535.html and word lime
expected = 0.15
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-535.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #216 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-535.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #216 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-535.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #217 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-535.html and word banana
expected = 0.05
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-535.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #217 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-535.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #217 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-535.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #218 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-535.html and word papaya
expected = 0.05
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-535.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #218 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-535.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #218 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-535.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #219 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-535.html and word blueberry
expected = 0.175
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-535.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #219 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-535.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #219 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-535.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #220 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-535.html and word fig
expected = 0.075
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-535.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #220 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-535.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #220 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-535.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #221 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-535.html and word tomato
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-535.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #221 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-535.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #221 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-535.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #222 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-311.html and word pear
expected = 0.07272727272727272
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-311.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #222 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-311.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #222 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-311.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #223 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-311.html and word apricot
expected = 0.07272727272727272
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-311.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #223 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-311.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #223 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-311.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #224 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-311.html and word kiwi
expected = 0.07272727272727272
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-311.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #224 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-311.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #224 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-311.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #225 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-311.html and word cherry
expected = 0.05454545454545454
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-311.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #225 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-311.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #225 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-311.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #226 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-311.html and word peach
expected = 0.05454545454545454
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-311.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #226 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-311.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #226 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-311.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #227 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-311.html and word lime
expected = 0.05454545454545454
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-311.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #227 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-311.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #227 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-311.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #228 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-311.html and word banana
expected = 0.07272727272727272
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-311.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #228 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-311.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #228 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-311.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #229 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-311.html and word papaya
expected = 0.07272727272727272
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-311.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #229 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-311.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #229 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-311.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #230 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-311.html and word blueberry
expected = 0.07272727272727272
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-311.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #230 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-311.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #230 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-311.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #231 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-311.html and word fig
expected = 0.07272727272727272
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-311.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #231 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-311.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #231 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-311.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #232 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-311.html and word tomato
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-311.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #232 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-311.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #232 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-311.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #233 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-139.html and word pear
expected = 0.16666666666666666
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-139.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #233 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-139.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #233 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-139.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #234 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-139.html and word apricot
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-139.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #234 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-139.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #234 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-139.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #235 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-139.html and word kiwi
expected = 0.08333333333333333
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-139.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #235 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-139.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #235 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-139.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #236 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-139.html and word cherry
expected = 0.08333333333333333
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-139.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #236 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-139.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #236 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-139.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #237 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-139.html and word peach
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-139.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #237 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-139.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #237 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-139.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #238 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-139.html and word lime
expected = 0.08333333333333333
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-139.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #238 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-139.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #238 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-139.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #239 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-139.html and word banana
expected = 0.16666666666666666
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-139.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #239 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-139.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #239 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-139.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #240 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-139.html and word papaya
expected = 0.08333333333333333
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-139.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #240 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-139.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #240 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-139.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #241 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-139.html and word blueberry
expected = 0.16666666666666666
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-139.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #241 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-139.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #241 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-139.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #242 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-139.html and word fig
expected = 0.08333333333333333
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-139.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #242 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-139.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #242 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-139.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #243 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-139.html and word tomato
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-139.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #243 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-139.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #243 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-139.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #244 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-347.html and word pear
expected = 0.03571428571428571
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-347.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #244 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-347.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #244 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-347.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #245 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-347.html and word apricot
expected = 0.07142857142857142
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-347.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #245 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-347.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #245 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-347.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #246 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-347.html and word kiwi
expected = 0.03571428571428571
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-347.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #246 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-347.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #246 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-347.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #247 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-347.html and word cherry
expected = 0.07142857142857142
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-347.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #247 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-347.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #247 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-347.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #248 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-347.html and word peach
expected = 0.07142857142857142
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-347.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #248 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-347.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #248 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-347.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #249 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-347.html and word lime
expected = 0.03571428571428571
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-347.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #249 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-347.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #249 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-347.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #250 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-347.html and word banana
expected = 0.07142857142857142
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-347.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #250 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-347.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #250 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-347.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #251 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-347.html and word papaya
expected = 0.03571428571428571
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-347.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #251 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-347.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #251 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-347.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #252 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-347.html and word blueberry
expected = 0.14285714285714285
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-347.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #252 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-347.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #252 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-347.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #253 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-347.html and word fig
expected = 0.07142857142857142
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-347.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #253 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-347.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #253 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-347.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #254 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-347.html and word tomato
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-347.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #254 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-347.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #254 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-347.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #255 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-529.html and word pear
expected = 0.10526315789473684
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-529.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #255 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-529.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #255 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-529.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #256 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-529.html and word apricot
expected = 0.05263157894736842
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-529.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #256 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-529.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #256 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-529.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #257 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-529.html and word kiwi
expected = 0.05263157894736842
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-529.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #257 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-529.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #257 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-529.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #258 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-529.html and word cherry
expected = 0.10526315789473684
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-529.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #258 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-529.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #258 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-529.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #259 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-529.html and word peach
expected = 0.05263157894736842
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-529.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #259 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-529.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #259 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-529.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #260 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-529.html and word lime
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-529.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #260 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-529.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #260 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-529.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #261 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-529.html and word banana
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-529.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #261 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-529.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #261 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-529.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #262 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-529.html and word papaya
expected = 0.05263157894736842
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-529.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #262 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-529.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #262 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-529.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #263 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-529.html and word blueberry
expected = 0.21052631578947367
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-529.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #263 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-529.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #263 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-529.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #264 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-529.html and word fig
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-529.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #264 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-529.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #264 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-529.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #265 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-529.html and word tomato
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-529.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #265 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-529.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #265 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-529.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #266 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-30.html and word pear
expected = 0.041666666666666664
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-30.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #266 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-30.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #266 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-30.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #267 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-30.html and word apricot
expected = 0.041666666666666664
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-30.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #267 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-30.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #267 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-30.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #268 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-30.html and word kiwi
expected = 0.10416666666666667
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-30.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #268 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-30.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #268 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-30.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #269 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-30.html and word cherry
expected = 0.08333333333333333
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-30.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #269 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-30.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #269 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-30.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #270 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-30.html and word peach
expected = 0.020833333333333332
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-30.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #270 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-30.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #270 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-30.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #271 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-30.html and word lime
expected = 0.10416666666666667
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-30.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #271 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-30.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #271 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-30.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #272 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-30.html and word banana
expected = 0.0625
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-30.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #272 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-30.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #272 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-30.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #273 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-30.html and word papaya
expected = 0.041666666666666664
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-30.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #273 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-30.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #273 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-30.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #274 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-30.html and word blueberry
expected = 0.10416666666666667
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-30.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #274 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-30.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #274 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-30.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #275 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-30.html and word fig
expected = 0.020833333333333332
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-30.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #275 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-30.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #275 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-30.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #276 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-30.html and word tomato
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-30.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #276 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-30.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #276 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-30.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #277 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word pear
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #277 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #277 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #278 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word apricot
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #278 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #278 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #279 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word kiwi
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #279 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #279 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #280 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word cherry
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #280 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #280 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #281 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word peach
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #281 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #281 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #282 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word lime
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #282 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #282 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #283 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word banana
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #283 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #283 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #284 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word papaya
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #284 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #284 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #285 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word blueberry
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #285 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #285 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #286 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word fig
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #286 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #286 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word fig\n\n')
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









output = open('fruits4-all-tfidf-failed.txt', 'w')
success_output = open('fruits4-all-tfidf-passed.txt', 'w')

#Test #288 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-416.html and word kiwi
expected = 0.0266468920738302
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-416.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #288 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-416.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #288 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-416.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #289 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-416.html and word fig
expected = 0.013807588118862324
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-416.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #289 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-416.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #289 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-416.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #290 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-416.html and word papaya
expected = 0.0034250880284858176
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-416.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #290 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-416.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #290 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-416.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #291 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-416.html and word peach
expected = 0.01762481974340443
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-416.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #291 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-416.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #291 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-416.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #292 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-416.html and word lime
expected = 0.02815520251728193
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-416.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #292 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-416.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #292 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-416.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #293 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-416.html and word apricot
expected = 0.01151324157474206
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-416.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #293 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-416.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #293 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-416.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #294 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-416.html and word orange
expected = 0.013550370054205254
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-416.html','orange')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #294 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-416.html and word orange\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #294 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-416.html and word orange\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #295 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-416.html and word blueberry
expected = 0.016825018818557077
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-416.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #295 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-416.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #295 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-416.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #296 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-416.html and word pear
expected = 0.013807588118862324
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-416.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #296 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-416.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #296 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-416.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #297 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-416.html and word banana
expected = 0.0225869353115785
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-416.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #297 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-416.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #297 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-416.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #298 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-416.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-416.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #298 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-416.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #298 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-416.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #299 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-789.html and word kiwi
expected = 0.014265458145399314
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-789.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #299 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-789.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #299 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-789.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #300 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-789.html and word fig
expected = 0.019022272044659654
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-789.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #300 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-789.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #300 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-789.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #301 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-789.html and word papaya
expected = 0.022903577831907183
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-789.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #301 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-789.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #301 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-789.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #302 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-789.html and word peach
expected = 0.014803166403464307
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-789.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #302 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-789.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #302 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-789.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #303 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-789.html and word lime
expected = 0.029330707725377474
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-789.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #303 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-789.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #303 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-789.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #304 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-789.html and word apricot
expected = 0.012006929407927653
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-789.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #304 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-789.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #304 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-789.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #305 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-789.html and word orange
expected = 0.004800779334180605
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-789.html','orange')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #305 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-789.html and word orange\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #305 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-789.html and word orange\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #306 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-789.html and word blueberry
expected = 0.014131409962687622
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-789.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #306 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-789.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #306 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-789.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #307 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-789.html and word pear
expected = 0.014399657538727077
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-789.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #307 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-789.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #307 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-789.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #308 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-789.html and word banana
expected = 0.02671779526008907
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-789.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #308 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-789.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #308 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-789.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #309 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-789.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-789.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #309 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-789.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #309 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-789.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #310 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-373.html and word kiwi
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-373.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #310 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-373.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #310 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-373.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #311 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-373.html and word fig
expected = 0.013999458213587683
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-373.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #311 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-373.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #311 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-373.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #312 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-373.html and word papaya
expected = 0.013608489848726587
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-373.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #312 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-373.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #312 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-373.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #313 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-373.html and word peach
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-373.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #313 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-373.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #313 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-373.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #314 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-373.html and word lime
expected = 0.02168656192332926
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-373.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #314 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-373.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #314 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-373.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #315 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-373.html and word apricot
expected = 0.01727527014550252
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-373.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #315 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-373.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #315 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-373.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #316 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-373.html and word orange
expected = 0.04507579008936898
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-373.html','orange')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #316 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-373.html and word orange\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #316 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-373.html and word orange\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #317 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-373.html and word blueberry
expected = 0.03911809536721924
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-373.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #317 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-373.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #317 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-373.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #318 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-373.html and word pear
expected = 0.013999458213587683
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-373.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #318 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-373.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #318 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-373.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #319 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-373.html and word banana
expected = 0.03800739435988355
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-373.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #319 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-373.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #319 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-373.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #320 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-373.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-373.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #320 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-373.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #320 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-373.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #321 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-163.html and word kiwi
expected = 0.019313975610119292
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-163.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #321 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-163.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #321 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-163.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #322 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-163.html and word fig
expected = 0.019495667903714584
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-163.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #322 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-163.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #322 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-163.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #323 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-163.html and word papaya
expected = 0.0215426553924889
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-163.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #323 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-163.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #323 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-163.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #324 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-163.html and word peach
expected = 0.014472195233256475
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-163.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #324 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-163.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #324 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-163.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #325 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-163.html and word lime
expected = 0.025959096581368683
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-163.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #325 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-163.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #325 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-163.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #326 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-163.html and word apricot
expected = 0.014009461983417813
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-163.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #326 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-163.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #326 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-163.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #327 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-163.html and word orange
expected = 0.016488266393375375
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-163.html','orange')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #327 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-163.html and word orange\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #327 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-163.html and word orange\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #328 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-163.html and word blueberry
expected = 0.011113438032975969
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-163.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #328 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-163.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #328 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-163.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #329 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-163.html and word pear
expected = 0.02741020640362533
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-163.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #329 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-163.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #329 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-163.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #330 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-163.html and word banana
expected = 0.013423188322938817
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-163.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #330 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-163.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #330 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-163.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #331 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-163.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-163.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #331 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-163.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #331 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-163.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #332 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-735.html and word kiwi
expected = 0.014772214810867533
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-735.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #332 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-735.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #332 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-735.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #333 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-735.html and word fig
expected = 0.020637005662867348
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-735.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #333 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-735.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #333 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-735.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #334 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-735.html and word papaya
expected = 0.022796895276510326
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-735.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #334 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-735.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #334 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-735.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #335 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-735.html and word peach
expected = 0.024109014415161154
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-735.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #335 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-735.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #335 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-735.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #336 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-735.html and word lime
expected = 0.02454836952178432
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-735.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #336 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-735.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #336 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-735.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #337 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-735.html and word apricot
expected = 0.017207844667044475
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-735.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #337 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-735.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #337 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-735.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #338 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-735.html and word orange
expected = 0.028448862802138115
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-735.html','orange')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #338 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-735.html and word orange\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #338 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-735.html and word orange\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #339 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-735.html and word blueberry
expected = 0.01745894831270778
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-735.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #339 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-735.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #339 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-735.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #340 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-735.html and word pear
expected = 0.0149111814143597
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-735.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #340 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-735.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #340 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-735.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #341 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-735.html and word banana
expected = 0.008631320152357059
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-735.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #341 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-735.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #341 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-735.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #342 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-735.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-735.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #342 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-735.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #342 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-735.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #343 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-685.html and word kiwi
expected = 0.029786273995702956
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-685.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #343 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-685.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #343 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-685.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #344 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-685.html and word fig
expected = 0.006998378416117431
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-685.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #344 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-685.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #344 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-685.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #345 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-685.html and word papaya
expected = 0.016665599142248334
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-685.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #345 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-685.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #345 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-685.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #346 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-685.html and word peach
expected = 0.034126253907250825
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-685.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #346 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-685.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #346 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-685.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #347 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-685.html and word lime
expected = 0.010913470426321379
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-685.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #347 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-685.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #347 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-685.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #348 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-685.html and word apricot
expected = 0.014295587897801531
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-685.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #348 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-685.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #348 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-685.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #349 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-685.html and word orange
expected = 0.013550370054205254
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-685.html','orange')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #349 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-685.html and word orange\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #349 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-685.html and word orange\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #350 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-685.html and word blueberry
expected = 0.0232469998128608
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-685.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #350 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-685.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #350 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-685.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #351 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-685.html and word pear
expected = 0.02368828283886138
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-685.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #351 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-685.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #351 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-685.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #352 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-685.html and word banana
expected = 0.0225869353115785
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-685.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #352 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-685.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #352 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-685.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #353 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-685.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-685.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #353 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-685.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #353 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-685.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #354 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-191.html and word kiwi
expected = 0.011346388939316525
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-191.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #354 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-191.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #354 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-191.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #355 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-191.html and word fig
expected = 0.01699017313790581
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-191.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #355 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-191.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #355 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-191.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #356 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-191.html and word papaya
expected = 0.01383926398426604
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-191.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #356 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-191.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #356 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-191.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #357 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-191.html and word peach
expected = 0.02848857144544599
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-191.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #357 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-191.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #357 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-191.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #358 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-191.html and word lime
expected = 0.02063546154499968
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-191.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #358 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-191.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #358 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-191.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #359 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-191.html and word apricot
expected = 0.011871185250485018
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-191.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #359 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-191.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #359 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-191.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #360 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-191.html and word orange
expected = 0.01397164752270901
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-191.html','orange')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #360 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-191.html and word orange\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #360 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-191.html and word orange\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #361 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-191.html and word blueberry
expected = 0.01934647588310838
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-191.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #361 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-191.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #361 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-191.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #362 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-191.html and word pear
expected = 0.022408132968047573
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-191.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #362 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-191.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #362 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-191.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #363 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-191.html and word banana
expected = 0.013574943060696364
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-191.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #363 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-191.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #363 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-191.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #364 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-191.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-191.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #364 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-191.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #364 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-191.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #365 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-795.html and word kiwi
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-795.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #365 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-795.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #365 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-795.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #366 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-795.html and word fig
expected = 0.02351268833659884
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-795.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #366 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-795.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #366 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-795.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #367 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-795.html and word papaya
expected = 0.017958080949304615
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-795.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #367 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-795.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #367 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-795.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #368 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-795.html and word peach
expected = 0.013706103136333603
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-795.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #368 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-795.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #368 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-795.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #369 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-795.html and word lime
expected = 0.016660564770298876
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-795.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #369 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-795.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #369 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-795.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #370 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-795.html and word apricot
expected = 0.015404266147012662
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-795.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #370 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-795.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #370 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-795.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #371 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-795.html and word orange
expected = 0.02061463256425605
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-795.html','orange')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #371 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-795.html and word orange\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #371 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-795.html and word orange\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #372 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-795.html and word blueberry
expected = 0.018129864239399888
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-795.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #372 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-795.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #372 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-795.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #373 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-795.html and word pear
expected = 0.028452560769748964
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-795.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #373 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-795.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #373 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-795.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #374 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-795.html and word banana
expected = 0.017615093305781395
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-795.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #374 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-795.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #374 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-795.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #375 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-795.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-795.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #375 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-795.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #375 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-795.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #376 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-912.html and word kiwi
expected = 0.03332644075666537
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-912.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #376 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-912.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #376 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-912.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #377 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-912.html and word fig
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-912.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #377 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-912.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #377 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-912.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #378 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-912.html and word papaya
expected = 0.03270047630602344
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-912.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #378 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-912.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #378 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-912.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #379 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-912.html and word peach
expected = 0.045154895482909706
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-912.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #379 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-912.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #379 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-912.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #380 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-912.html and word lime
expected = 0.023989673200479275
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-912.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #380 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-912.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #380 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-912.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #381 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-912.html and word apricot
expected = 0.01910990256112388
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-912.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #381 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-912.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #381 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-912.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #382 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-912.html and word orange
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-912.html','orange')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #382 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-912.html and word orange\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #382 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-912.html and word orange\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #383 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-912.html and word blueberry
expected = 0.011501253590558008
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-912.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #383 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-912.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #383 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-912.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #384 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-912.html and word pear
expected = 0.011719574579420997
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-912.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #384 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-912.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #384 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-912.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #385 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-912.html and word banana
expected = 0.021852564313417096
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-912.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #385 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-912.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #385 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-912.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #386 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-912.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-912.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #386 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-912.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #386 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-912.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #387 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-548.html and word kiwi
expected = 0.023787283262202967
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-548.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #387 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-548.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #387 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-548.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #388 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-548.html and word fig
expected = 0.012291482707434161
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-548.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #388 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-548.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #388 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-548.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #389 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-548.html and word papaya
expected = 0.02334049106473404
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-548.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #389 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-548.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #389 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-548.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #390 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-548.html and word peach
expected = 0.018729959700589112
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-548.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #390 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-548.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #390 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-548.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #391 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-548.html and word lime
expected = 0.01286618901936256
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-548.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #391 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-548.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #391 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-548.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #392 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-548.html and word apricot
expected = 0.024741984592812714
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-548.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #392 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-548.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #392 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-548.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #393 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-548.html and word orange
expected = 0.012062507786792295
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-548.html','orange')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #393 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-548.html and word orange\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #393 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-548.html and word orange\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #394 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-548.html and word blueberry
expected = 0.023563761377350296
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-548.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #394 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-548.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #394 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-548.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #395 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-548.html and word pear
expected = 0.006220696851970735
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-548.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #395 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-548.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #395 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-548.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #396 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-548.html and word banana
expected = 0.01172001055056407
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-548.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #396 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-548.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #396 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-548.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #397 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-548.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-548.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #397 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-548.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #397 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-548.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #398 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word kiwi
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #398 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #398 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #399 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word fig
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #399 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #399 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #400 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word papaya
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #400 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #400 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #401 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word peach
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #401 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #401 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #402 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word lime
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #402 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #402 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #403 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word apricot
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #403 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #403 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #404 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word orange
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','orange')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #404 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word orange\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #404 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word orange\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #405 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word blueberry
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #405 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #405 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #406 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word pear
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #406 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #406 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #407 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word banana
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #407 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #407 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word banana\n\n')
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









output = open('fruits4-all-search-failed.txt', 'w')
success_output = open('fruits4-all-search-passed.txt', 'w')

#Test #409 checking search results for 'coconut blueberry papaya cherry lime lime lime fig' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-724.html', 'title': 'N-724', 'score': 0.988938794131589}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-86.html', 'title': 'N-86', 'score': 0.9865162973352115}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-269.html', 'title': 'N-269', 'score': 0.98081317155367}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-78.html', 'title': 'N-78', 'score': 0.9807370632371006}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-308.html', 'title': 'N-308', 'score': 0.9777283395626623}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-989.html', 'title': 'N-989', 'score': 0.9752292663913917}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-140.html', 'title': 'N-140', 'score': 0.9738773987726054}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-231.html', 'title': 'N-231', 'score': 0.973098285660905}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-166.html', 'title': 'N-166', 'score': 0.9729197151849707}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-707.html', 'title': 'N-707', 'score': 0.9711396464635533}]
result = search.search('coconut blueberry papaya cherry lime lime lime fig',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #409 checking search results for 'coconut blueberry papaya cherry lime lime lime fig' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #409 checking search results for 'coconut blueberry papaya cherry lime lime lime fig' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #410 checking search results for 'lime apricot apple banana banana banana blueberry blueberry' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-887.html', 'title': 'N-887', 'score': 0.9900312806082066}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-736.html', 'title': 'N-736', 'score': 0.9878152834097609}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-987.html', 'title': 'N-987', 'score': 0.9854313489080031}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-356.html', 'title': 'N-356', 'score': 0.9850795524399755}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-675.html', 'title': 'N-675', 'score': 0.984244308760103}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-252.html', 'title': 'N-252', 'score': 0.9821646133567361}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-538.html', 'title': 'N-538', 'score': 0.9816545182731169}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-450.html', 'title': 'N-450', 'score': 0.9798431062109367}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-805.html', 'title': 'N-805', 'score': 0.9788644709758815}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-937.html', 'title': 'N-937', 'score': 0.9778841486170977}]
result = search.search('lime apricot apple banana banana banana blueberry blueberry',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #410 checking search results for 'lime apricot apple banana banana banana blueberry blueberry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #410 checking search results for 'lime apricot apple banana banana banana blueberry blueberry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #411 checking search results for 'coconut pear fig blueberry' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-826.html', 'title': 'N-826', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-329.html', 'title': 'N-329', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-177.html', 'title': 'N-177', 'score': 0.9984261077056125}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-542.html', 'title': 'N-542', 'score': 0.9983951759314037}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-662.html', 'title': 'N-662', 'score': 0.9979604220768858}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-165.html', 'title': 'N-165', 'score': 0.9979480695369091}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-656.html', 'title': 'N-656', 'score': 0.9978390857425533}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-154.html', 'title': 'N-154', 'score': 0.9978137375969804}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-394.html', 'title': 'N-394', 'score': 0.9973709906217061}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-258.html', 'title': 'N-258', 'score': 0.9972441592171736}]
result = search.search('coconut pear fig blueberry',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #411 checking search results for 'coconut pear fig blueberry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #411 checking search results for 'coconut pear fig blueberry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #412 checking search results for 'kiwi pear apple apple kiwi orange kiwi cherry' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-901.html', 'title': 'N-901', 'score': 0.9978902601495842}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-801.html', 'title': 'N-801', 'score': 0.9958808108471641}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-295.html', 'title': 'N-295', 'score': 0.9929599408349623}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-8.html', 'title': 'N-8', 'score': 0.9927939123036377}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-818.html', 'title': 'N-818', 'score': 0.9916944049193307}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-339.html', 'title': 'N-339', 'score': 0.9907601052718299}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-361.html', 'title': 'N-361', 'score': 0.9905740444143547}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-949.html', 'title': 'N-949', 'score': 0.9899619730176435}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-571.html', 'title': 'N-571', 'score': 0.9878369759876208}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html', 'title': 'N-3', 'score': 0.9857052387529256}]
result = search.search('kiwi pear apple apple kiwi orange kiwi cherry',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #412 checking search results for 'kiwi pear apple apple kiwi orange kiwi cherry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #412 checking search results for 'kiwi pear apple apple kiwi orange kiwi cherry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #413 checking search results for 'blueberry coconut papaya pear papaya coconut apple' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-845.html', 'title': 'N-845', 'score': 0.9972608907927933}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-774.html', 'title': 'N-774', 'score': 0.995819002017635}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-962.html', 'title': 'N-962', 'score': 0.9954592331541893}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-620.html', 'title': 'N-620', 'score': 0.9952766508616085}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-2.html', 'title': 'N-2', 'score': 0.9952284960950668}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-722.html', 'title': 'N-722', 'score': 0.9948664922341994}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-427.html', 'title': 'N-427', 'score': 0.9942512139792072}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-493.html', 'title': 'N-493', 'score': 0.9942308512786028}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-696.html', 'title': 'N-696', 'score': 0.9927550681325102}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-519.html', 'title': 'N-519', 'score': 0.9923505195109654}]
result = search.search('blueberry coconut papaya pear papaya coconut apple',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #413 checking search results for 'blueberry coconut papaya pear papaya coconut apple' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #413 checking search results for 'blueberry coconut papaya pear papaya coconut apple' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #414 checking search results for 'orange blueberry orange kiwi coconut kiwi tomato papaya' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-849.html', 'title': 'N-849', 'score': 0.9948158509483247}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-925.html', 'title': 'N-925', 'score': 0.9945030381294049}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-378.html', 'title': 'N-378', 'score': 0.9896901236879464}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-590.html', 'title': 'N-590', 'score': 0.9896034728778715}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-377.html', 'title': 'N-377', 'score': 0.9895382651727317}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-482.html', 'title': 'N-482', 'score': 0.9892670680970707}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-317.html', 'title': 'N-317', 'score': 0.9883066853719368}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-892.html', 'title': 'N-892', 'score': 0.9881091877103944}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-37.html', 'title': 'N-37', 'score': 0.9875108824186533}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-266.html', 'title': 'N-266', 'score': 0.9872438340607811}]
result = search.search('orange blueberry orange kiwi coconut kiwi tomato papaya',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #414 checking search results for 'orange blueberry orange kiwi coconut kiwi tomato papaya' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #414 checking search results for 'orange blueberry orange kiwi coconut kiwi tomato papaya' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #415 checking search results for 'coconut pear apricot pear cherry coconut peach apricot' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-177.html', 'title': 'N-177', 'score': 0.9977868332239724}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-964.html', 'title': 'N-964', 'score': 0.9965565019773377}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-9.html', 'title': 'N-9', 'score': 0.9948246904461647}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-886.html', 'title': 'N-886', 'score': 0.9946922925082218}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-531.html', 'title': 'N-531', 'score': 0.9937140787368639}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-251.html', 'title': 'N-251', 'score': 0.9934693523500311}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-956.html', 'title': 'N-956', 'score': 0.9934691626944877}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-704.html', 'title': 'N-704', 'score': 0.9933495439322872}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-52.html', 'title': 'N-52', 'score': 0.9926340430519888}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-869.html', 'title': 'N-869', 'score': 0.9926169985367451}]
result = search.search('coconut pear apricot pear cherry coconut peach apricot',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #415 checking search results for 'coconut pear apricot pear cherry coconut peach apricot' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #415 checking search results for 'coconut pear apricot pear cherry coconut peach apricot' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #416 checking search results for 'papaya blueberry papaya orange fig pear tomato kiwi' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-845.html', 'title': 'N-845', 'score': 0.9968263913424908}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-13.html', 'title': 'N-13', 'score': 0.995577239600366}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-551.html', 'title': 'N-551', 'score': 0.9924764990107031}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-722.html', 'title': 'N-722', 'score': 0.9914426424846029}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-97.html', 'title': 'N-97', 'score': 0.9907677679726355}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-337.html', 'title': 'N-337', 'score': 0.9904585116671383}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-226.html', 'title': 'N-226', 'score': 0.9866393145485556}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-929.html', 'title': 'N-929', 'score': 0.9856711166242452}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-740.html', 'title': 'N-740', 'score': 0.9853177420630078}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-177.html', 'title': 'N-177', 'score': 0.9849188656378783}]
result = search.search('papaya blueberry papaya orange fig pear tomato kiwi',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #416 checking search results for 'papaya blueberry papaya orange fig pear tomato kiwi' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #416 checking search results for 'papaya blueberry papaya orange fig pear tomato kiwi' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #417 checking search results for 'banana banana kiwi orange lime peach papaya banana' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-557.html', 'title': 'N-557', 'score': 0.9891492447574142}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-991.html', 'title': 'N-991', 'score': 0.9872756913550716}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-43.html', 'title': 'N-43', 'score': 0.9814881545046786}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-802.html', 'title': 'N-802', 'score': 0.9806780826765202}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-276.html', 'title': 'N-276', 'score': 0.9778168817259193}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-356.html', 'title': 'N-356', 'score': 0.9766063010263308}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-792.html', 'title': 'N-792', 'score': 0.973761527719561}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-386.html', 'title': 'N-386', 'score': 0.9737068315956017}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-468.html', 'title': 'N-468', 'score': 0.9726341587422885}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-382.html', 'title': 'N-382', 'score': 0.9714969986824923}]
result = search.search('banana banana kiwi orange lime peach papaya banana',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #417 checking search results for 'banana banana kiwi orange lime peach papaya banana' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #417 checking search results for 'banana banana kiwi orange lime peach papaya banana' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #418 checking search results for 'pear pear papaya pear peach coconut coconut' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-270.html', 'title': 'N-270', 'score': 0.9969975899970656}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-971.html', 'title': 'N-971', 'score': 0.9969974336007404}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-716.html', 'title': 'N-716', 'score': 0.9968059548224121}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-897.html', 'title': 'N-897', 'score': 0.9946217677361093}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-763.html', 'title': 'N-763', 'score': 0.992200886482511}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-448.html', 'title': 'N-448', 'score': 0.9919793064275084}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-291.html', 'title': 'N-291', 'score': 0.9894961245034246}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-395.html', 'title': 'N-395', 'score': 0.9874596936471766}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-51.html', 'title': 'N-51', 'score': 0.9860390357000214}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-391.html', 'title': 'N-391', 'score': 0.9860123234624876}]
result = search.search('pear pear papaya pear peach coconut coconut',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #418 checking search results for 'pear pear papaya pear peach coconut coconut' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #418 checking search results for 'pear pear papaya pear peach coconut coconut' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #419 checking search results for 'papaya coconut lime blueberry' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-317.html', 'title': 'N-317', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-935.html', 'title': 'N-935', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-403.html', 'title': 'N-403', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-281.html', 'title': 'N-281', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-53.html', 'title': 'N-53', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-731.html', 'title': 'N-731', 'score': 0.9988073737776327}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-957.html', 'title': 'N-957', 'score': 0.9987979376180459}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-530.html', 'title': 'N-530', 'score': 0.9976826566190012}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-394.html', 'title': 'N-394', 'score': 0.997501291906714}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-590.html', 'title': 'N-590', 'score': 0.9972155100666359}]
result = search.search('papaya coconut lime blueberry',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #419 checking search results for 'papaya coconut lime blueberry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #419 checking search results for 'papaya coconut lime blueberry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #420 checking search results for 'peach banana orange tomato pear apple orange' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-7.html', 'title': 'N-7', 'score': 0.9987795447842092}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-974.html', 'title': 'N-974', 'score': 0.9963255736883901}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-237.html', 'title': 'N-237', 'score': 0.9945769450866171}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-804.html', 'title': 'N-804', 'score': 0.9945749285952591}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-975.html', 'title': 'N-975', 'score': 0.9922187920910764}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-67.html', 'title': 'N-67', 'score': 0.9907852897799718}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-26.html', 'title': 'N-26', 'score': 0.9902369165088282}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-129.html', 'title': 'N-129', 'score': 0.9869054824108482}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-612.html', 'title': 'N-612', 'score': 0.9863436099889353}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-239.html', 'title': 'N-239', 'score': 0.9860602095636959}]
result = search.search('peach banana orange tomato pear apple orange',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #420 checking search results for 'peach banana orange tomato pear apple orange' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #420 checking search results for 'peach banana orange tomato pear apple orange' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #421 checking search results for 'apple pear pear fig peach pear apricot' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html', 'title': 'N-3', 'score': 0.014587086668103332}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html', 'title': 'N-1', 'score': 0.01433745784912093}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html', 'title': 'N-0', 'score': 0.01220934133420177}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-12.html', 'title': 'N-12', 'score': 0.01060981697606083}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-6.html', 'title': 'N-6', 'score': 0.009203632186970876}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-4.html', 'title': 'N-4', 'score': 0.008136107084276248}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-15.html', 'title': 'N-15', 'score': 0.00680756223416553}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-8.html', 'title': 'N-8', 'score': 0.005981960932807195}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-9.html', 'title': 'N-9', 'score': 0.005857697854670999}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-32.html', 'title': 'N-32', 'score': 0.005766813285050636}]
result = search.search('apple pear pear fig peach pear apricot',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #421 checking search results for 'apple pear pear fig peach pear apricot' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #421 checking search results for 'apple pear pear fig peach pear apricot' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #422 checking search results for 'apple pear pear fig peach pear apricot' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-448.html', 'title': 'N-448', 'score': 0.9994907012787279}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-889.html', 'title': 'N-889', 'score': 0.992892842015196}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-925.html', 'title': 'N-925', 'score': 0.9923524685825571}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-41.html', 'title': 'N-41', 'score': 0.9894669153451692}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-480.html', 'title': 'N-480', 'score': 0.9892458777742528}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-575.html', 'title': 'N-575', 'score': 0.9886109251144515}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-291.html', 'title': 'N-291', 'score': 0.9874890079545307}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-563.html', 'title': 'N-563', 'score': 0.9859047069635382}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-724.html', 'title': 'N-724', 'score': 0.9848854641171375}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-545.html', 'title': 'N-545', 'score': 0.9838063363026532}]
result = search.search('apple pear pear fig peach pear apricot',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #422 checking search results for 'apple pear pear fig peach pear apricot' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #422 checking search results for 'apple pear pear fig peach pear apricot' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #423 checking search results for 'fig kiwi blueberry pear pear pear blueberry papaya' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-72.html', 'title': 'N-72', 'score': 0.9943232088894668}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-522.html', 'title': 'N-522', 'score': 0.9907533752872013}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-448.html', 'title': 'N-448', 'score': 0.990478340893507}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-971.html', 'title': 'N-971', 'score': 0.9895760244237459}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-885.html', 'title': 'N-885', 'score': 0.9891087118366303}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-582.html', 'title': 'N-582', 'score': 0.9881287562890742}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-838.html', 'title': 'N-838', 'score': 0.9877505699403294}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-395.html', 'title': 'N-395', 'score': 0.987676952766705}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-557.html', 'title': 'N-557', 'score': 0.9875042149275632}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-380.html', 'title': 'N-380', 'score': 0.9870866562503491}]
result = search.search('fig kiwi blueberry pear pear pear blueberry papaya',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #423 checking search results for 'fig kiwi blueberry pear pear pear blueberry papaya' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #423 checking search results for 'fig kiwi blueberry pear pear pear blueberry papaya' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #424 checking search results for 'banana tomato blueberry cherry blueberry fig' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-347.html', 'title': 'N-347', 'score': 0.9998352945922115}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-945.html', 'title': 'N-945', 'score': 0.9998352945922115}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-977.html', 'title': 'N-977', 'score': 0.999786427592591}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-460.html', 'title': 'N-460', 'score': 0.9982930007878185}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-961.html', 'title': 'N-961', 'score': 0.9970185030741523}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-988.html', 'title': 'N-988', 'score': 0.9964726812056584}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-540.html', 'title': 'N-540', 'score': 0.9963183072886023}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-340.html', 'title': 'N-340', 'score': 0.9961405464171649}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-903.html', 'title': 'N-903', 'score': 0.9961245551525517}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-57.html', 'title': 'N-57', 'score': 0.9957998559698698}]
result = search.search('banana tomato blueberry cherry blueberry fig',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #424 checking search results for 'banana tomato blueberry cherry blueberry fig' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #424 checking search results for 'banana tomato blueberry cherry blueberry fig' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #425 checking search results for 'cherry blueberry banana tomato cherry cherry' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-888.html', 'title': 'N-888', 'score': 0.9996917091900457}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-930.html', 'title': 'N-930', 'score': 0.9995768388712784}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-434.html', 'title': 'N-434', 'score': 0.9992915676458631}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-4.html', 'title': 'N-4', 'score': 0.9979930392537035}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-380.html', 'title': 'N-380', 'score': 0.9977474587333548}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-482.html', 'title': 'N-482', 'score': 0.9976842068798091}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-241.html', 'title': 'N-241', 'score': 0.9976119077802348}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-379.html', 'title': 'N-379', 'score': 0.9975858913035869}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-849.html', 'title': 'N-849', 'score': 0.997550131021151}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-192.html', 'title': 'N-192', 'score': 0.9974712130127855}]
result = search.search('cherry blueberry banana tomato cherry cherry',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #425 checking search results for 'cherry blueberry banana tomato cherry cherry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #425 checking search results for 'cherry blueberry banana tomato cherry cherry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #426 checking search results for 'lime blueberry papaya orange banana fig apple' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-285.html', 'title': 'N-285', 'score': 0.994715965979303}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-662.html', 'title': 'N-662', 'score': 0.9932168423825521}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-795.html', 'title': 'N-795', 'score': 0.9930905832653052}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-950.html', 'title': 'N-950', 'score': 0.991866362512287}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-967.html', 'title': 'N-967', 'score': 0.9914087707516864}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-530.html', 'title': 'N-530', 'score': 0.9906396595636604}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-971.html', 'title': 'N-971', 'score': 0.9896378077027165}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-916.html', 'title': 'N-916', 'score': 0.989342322535108}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-258.html', 'title': 'N-258', 'score': 0.9873200335282065}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-380.html', 'title': 'N-380', 'score': 0.9868741977867718}]
result = search.search('lime blueberry papaya orange banana fig apple',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #426 checking search results for 'lime blueberry papaya orange banana fig apple' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #426 checking search results for 'lime blueberry papaya orange banana fig apple' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #427 checking search results for 'tomato apricot kiwi cherry apricot blueberry apple' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-660.html', 'title': 'N-660', 'score': 0.9969821396435571}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-411.html', 'title': 'N-411', 'score': 0.9954636866293555}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-196.html', 'title': 'N-196', 'score': 0.9947214465513418}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-24.html', 'title': 'N-24', 'score': 0.9937639257419788}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-9.html', 'title': 'N-9', 'score': 0.9936934234869759}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-143.html', 'title': 'N-143', 'score': 0.993481869871053}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-676.html', 'title': 'N-676', 'score': 0.9924057185903684}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-267.html', 'title': 'N-267', 'score': 0.9917783773553518}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-470.html', 'title': 'N-470', 'score': 0.9908363704422338}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-386.html', 'title': 'N-386', 'score': 0.9908320359034292}]
result = search.search('tomato apricot kiwi cherry apricot blueberry apple',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #427 checking search results for 'tomato apricot kiwi cherry apricot blueberry apple' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #427 checking search results for 'tomato apricot kiwi cherry apricot blueberry apple' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #428 checking search results for 'peach lime peach blueberry apple banana' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-434.html', 'title': 'N-434', 'score': 0.9997816912965146}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-501.html', 'title': 'N-501', 'score': 0.9962433131840686}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-267.html', 'title': 'N-267', 'score': 0.995731271187061}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-220.html', 'title': 'N-220', 'score': 0.9947619600744806}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-93.html', 'title': 'N-93', 'score': 0.9934126048890466}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-84.html', 'title': 'N-84', 'score': 0.9926929483263639}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-774.html', 'title': 'N-774', 'score': 0.9911850457696426}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-834.html', 'title': 'N-834', 'score': 0.9902495585122325}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-819.html', 'title': 'N-819', 'score': 0.9901228530036212}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-753.html', 'title': 'N-753', 'score': 0.9899045165995427}]
result = search.search('peach lime peach blueberry apple banana',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #428 checking search results for 'peach lime peach blueberry apple banana' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #428 checking search results for 'peach lime peach blueberry apple banana' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #429 checking search results for 'peach orange fig apricot blueberry lime' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-385.html', 'title': 'N-385', 'score': 0.9967870281491479}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-818.html', 'title': 'N-818', 'score': 0.9962152220486625}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-154.html', 'title': 'N-154', 'score': 0.9941635538489095}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-967.html', 'title': 'N-967', 'score': 0.9930646958628412}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-662.html', 'title': 'N-662', 'score': 0.9920694324856544}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-783.html', 'title': 'N-783', 'score': 0.991918895171308}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-488.html', 'title': 'N-488', 'score': 0.9918388909548147}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-466.html', 'title': 'N-466', 'score': 0.991110665315959}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-157.html', 'title': 'N-157', 'score': 0.9909455316416185}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-686.html', 'title': 'N-686', 'score': 0.9909424924718544}]
result = search.search('peach orange fig apricot blueberry lime',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #429 checking search results for 'peach orange fig apricot blueberry lime' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #429 checking search results for 'peach orange fig apricot blueberry lime' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #430 checking search results for 'pear apple apple coconut fig banana blueberry' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-311.html', 'title': 'N-311', 'score': 0.9962365656592456}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-639.html', 'title': 'N-639', 'score': 0.9946134742703531}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-90.html', 'title': 'N-90', 'score': 0.9945090799851035}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-13.html', 'title': 'N-13', 'score': 0.9926903979722327}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-826.html', 'title': 'N-826', 'score': 0.9919036825628249}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-766.html', 'title': 'N-766', 'score': 0.9917866434059378}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-601.html', 'title': 'N-601', 'score': 0.9891834283599911}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-336.html', 'title': 'N-336', 'score': 0.987275140938233}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-559.html', 'title': 'N-559', 'score': 0.9868122076597275}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-921.html', 'title': 'N-921', 'score': 0.9865070295041319}]
result = search.search('pear apple apple coconut fig banana blueberry',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #430 checking search results for 'pear apple apple coconut fig banana blueberry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #430 checking search results for 'pear apple apple coconut fig banana blueberry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #431 checking search results for 'orange banana blueberry blueberry blueberry peach banana' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-114.html', 'title': 'N-114', 'score': 0.9981003976657419}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-500.html', 'title': 'N-500', 'score': 0.9969318820568438}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-366.html', 'title': 'N-366', 'score': 0.9950871701174999}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-167.html', 'title': 'N-167', 'score': 0.9950138673973112}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-287.html', 'title': 'N-287', 'score': 0.9930543547309184}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-750.html', 'title': 'N-750', 'score': 0.9928295982361031}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-364.html', 'title': 'N-364', 'score': 0.9920012742053709}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-965.html', 'title': 'N-965', 'score': 0.9912318054518454}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-222.html', 'title': 'N-222', 'score': 0.9901082946793239}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-113.html', 'title': 'N-113', 'score': 0.9894796222622978}]
result = search.search('orange banana blueberry blueberry blueberry peach banana',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #431 checking search results for 'orange banana blueberry blueberry blueberry peach banana' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #431 checking search results for 'orange banana blueberry blueberry blueberry peach banana' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #432 checking search results for 'fig pear lime papaya' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-61.html', 'title': 'N-61', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-340.html', 'title': 'N-340', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-138.html', 'title': 'N-138', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-258.html', 'title': 'N-258', 'score': 0.9982803493882726}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-488.html', 'title': 'N-488', 'score': 0.9981015123900968}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-135.html', 'title': 'N-135', 'score': 0.9976548794792834}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-398.html', 'title': 'N-398', 'score': 0.9973189940791447}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-965.html', 'title': 'N-965', 'score': 0.9972099533002826}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-366.html', 'title': 'N-366', 'score': 0.996344961703768}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-394.html', 'title': 'N-394', 'score': 0.9961887988265301}]
result = search.search('fig pear lime papaya',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #432 checking search results for 'fig pear lime papaya' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #432 checking search results for 'fig pear lime papaya' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #433 checking search results for 'fig orange lime lime kiwi apricot' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-72.html', 'title': 'N-72', 'score': 0.9983754945449235}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-253.html', 'title': 'N-253', 'score': 0.9970958312757553}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-350.html', 'title': 'N-350', 'score': 0.9955784263118974}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-812.html', 'title': 'N-812', 'score': 0.9935786725010716}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-372.html', 'title': 'N-372', 'score': 0.9933602375064953}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-231.html', 'title': 'N-231', 'score': 0.9907662105240107}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-766.html', 'title': 'N-766', 'score': 0.989670727452102}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-73.html', 'title': 'N-73', 'score': 0.9894818978484483}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-724.html', 'title': 'N-724', 'score': 0.9882508561972849}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-750.html', 'title': 'N-750', 'score': 0.988220165986897}]
result = search.search('fig orange lime lime kiwi apricot',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #433 checking search results for 'fig orange lime lime kiwi apricot' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #433 checking search results for 'fig orange lime lime kiwi apricot' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #434 checking search results for 'banana blueberry peach apricot lime papaya papaya' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-230.html', 'title': 'N-230', 'score': 0.9972659887561159}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-344.html', 'title': 'N-344', 'score': 0.9963878900066315}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-410.html', 'title': 'N-410', 'score': 0.9942740713431668}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-620.html', 'title': 'N-620', 'score': 0.9937318891702387}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-826.html', 'title': 'N-826', 'score': 0.9911140232683291}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-515.html', 'title': 'N-515', 'score': 0.9906700724508435}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-2.html', 'title': 'N-2', 'score': 0.9890827022543167}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-91.html', 'title': 'N-91', 'score': 0.9884287843384705}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-728.html', 'title': 'N-728', 'score': 0.9871920764101194}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-186.html', 'title': 'N-186', 'score': 0.9866672442205391}]
result = search.search('banana blueberry peach apricot lime papaya papaya',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #434 checking search results for 'banana blueberry peach apricot lime papaya papaya' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #434 checking search results for 'banana blueberry peach apricot lime papaya papaya' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #435 checking search results for 'blueberry lime blueberry coconut cherry kiwi papaya blueberry' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-517.html', 'title': 'N-517', 'score': 0.9996933246910892}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-769.html', 'title': 'N-769', 'score': 0.990530094336491}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-798.html', 'title': 'N-798', 'score': 0.9889118120460934}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-979.html', 'title': 'N-979', 'score': 0.985261339824464}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-557.html', 'title': 'N-557', 'score': 0.9790713831793391}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-340.html', 'title': 'N-340', 'score': 0.9769474307357028}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-424.html', 'title': 'N-424', 'score': 0.975500957207456}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-963.html', 'title': 'N-963', 'score': 0.973953852329509}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-288.html', 'title': 'N-288', 'score': 0.9721670928604437}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-126.html', 'title': 'N-126', 'score': 0.9713866756303029}]
result = search.search('blueberry lime blueberry coconut cherry kiwi papaya blueberry',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #435 checking search results for 'blueberry lime blueberry coconut cherry kiwi papaya blueberry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #435 checking search results for 'blueberry lime blueberry coconut cherry kiwi papaya blueberry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #436 checking search results for 'apricot coconut orange fig lime lime lime' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-189.html', 'title': 'N-189', 'score': 0.9995114093830024}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-92.html', 'title': 'N-92', 'score': 0.9948338019447995}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-724.html', 'title': 'N-724', 'score': 0.9948209203842885}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-707.html', 'title': 'N-707', 'score': 0.9947536680715168}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-86.html', 'title': 'N-86', 'score': 0.9910015079011862}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-989.html', 'title': 'N-989', 'score': 0.9898588590425672}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-253.html', 'title': 'N-253', 'score': 0.9897079762535614}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-231.html', 'title': 'N-231', 'score': 0.9870187687005629}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-571.html', 'title': 'N-571', 'score': 0.9837770543748793}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-341.html', 'title': 'N-341', 'score': 0.9823539824240567}]
result = search.search('apricot coconut orange fig lime lime lime',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #436 checking search results for 'apricot coconut orange fig lime lime lime' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #436 checking search results for 'apricot coconut orange fig lime lime lime' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #437 checking search results for 'papaya blueberry lime tomato banana pear blueberry lime' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-147.html', 'title': 'N-147', 'score': 0.9999638190170882}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-619.html', 'title': 'N-619', 'score': 0.9999236797013208}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-445.html', 'title': 'N-445', 'score': 0.9981078032925828}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-466.html', 'title': 'N-466', 'score': 0.995491255643185}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-30.html', 'title': 'N-30', 'score': 0.9944231401588797}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-761.html', 'title': 'N-761', 'score': 0.9931527084907843}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-385.html', 'title': 'N-385', 'score': 0.9930319258527365}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-783.html', 'title': 'N-783', 'score': 0.9929217128199631}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-832.html', 'title': 'N-832', 'score': 0.992423305108081}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-922.html', 'title': 'N-922', 'score': 0.9920528579213108}]
result = search.search('papaya blueberry lime tomato banana pear blueberry lime',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #437 checking search results for 'papaya blueberry lime tomato banana pear blueberry lime' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #437 checking search results for 'papaya blueberry lime tomato banana pear blueberry lime' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #438 checking search results for 'lime coconut cherry blueberry fig lime lime cherry' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html', 'title': 'N-3', 'score': 0.016644912069670982}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html', 'title': 'N-1', 'score': 0.015198447090440149}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html', 'title': 'N-0', 'score': 0.013068999040431855}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-12.html', 'title': 'N-12', 'score': 0.012114653744813977}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-6.html', 'title': 'N-6', 'score': 0.010058084519785904}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-4.html', 'title': 'N-4', 'score': 0.0074013356187864554}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-15.html', 'title': 'N-15', 'score': 0.006663199136691491}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-8.html', 'title': 'N-8', 'score': 0.006538423235720996}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-9.html', 'title': 'N-9', 'score': 0.006004097877162714}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-32.html', 'title': 'N-32', 'score': 0.00587112648670198}]
result = search.search('lime coconut cherry blueberry fig lime lime cherry',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #438 checking search results for 'lime coconut cherry blueberry fig lime lime cherry' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #438 checking search results for 'lime coconut cherry blueberry fig lime lime cherry' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #439 checking search results for 'pear apple pear coconut orange' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-383.html', 'title': 'N-383', 'score': 0.998819830270958}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-562.html', 'title': 'N-562', 'score': 0.9981368621404488}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-398.html', 'title': 'N-398', 'score': 0.9973410218359009}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-794.html', 'title': 'N-794', 'score': 0.9964812746202182}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-538.html', 'title': 'N-538', 'score': 0.9964351358698288}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-41.html', 'title': 'N-41', 'score': 0.9963705315126442}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-724.html', 'title': 'N-724', 'score': 0.9962336649748342}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-344.html', 'title': 'N-344', 'score': 0.9957119167158813}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-699.html', 'title': 'N-699', 'score': 0.9949601328458858}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-72.html', 'title': 'N-72', 'score': 0.9949245818885557}]
result = search.search('pear apple pear coconut orange',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #439 checking search results for 'pear apple pear coconut orange' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #439 checking search results for 'pear apple pear coconut orange' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #440 checking search results for 'apricot papaya peach kiwi coconut apple coconut' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-686.html', 'title': 'N-686', 'score': 0.9968721197572686}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-913.html', 'title': 'N-913', 'score': 0.9954939280993405}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-395.html', 'title': 'N-395', 'score': 0.9950893694002716}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-143.html', 'title': 'N-143', 'score': 0.9928303063575704}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-152.html', 'title': 'N-152', 'score': 0.9920567574617272}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-721.html', 'title': 'N-721', 'score': 0.9910718025601818}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-77.html', 'title': 'N-77', 'score': 0.9909377719808139}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-567.html', 'title': 'N-567', 'score': 0.9902661525107832}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-438.html', 'title': 'N-438', 'score': 0.9902410070070369}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-611.html', 'title': 'N-611', 'score': 0.9900039682116575}]
result = search.search('apricot papaya peach kiwi coconut apple coconut',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #440 checking search results for 'apricot papaya peach kiwi coconut apple coconut' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #440 checking search results for 'apricot papaya peach kiwi coconut apple coconut' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #441 checking search results for 'apricot kiwi lime coconut coconut apricot apple apple' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-17.html', 'title': 'N-17', 'score': 0.996835946344054}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-741.html', 'title': 'N-741', 'score': 0.9965539863250872}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-720.html', 'title': 'N-720', 'score': 0.9938065009080657}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-931.html', 'title': 'N-931', 'score': 0.9936757424027469}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-41.html', 'title': 'N-41', 'score': 0.992247705540813}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-531.html', 'title': 'N-531', 'score': 0.990807711751935}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-433.html', 'title': 'N-433', 'score': 0.9902873285210942}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-956.html', 'title': 'N-956', 'score': 0.9890228251265707}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-647.html', 'title': 'N-647', 'score': 0.9878261305296597}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-66.html', 'title': 'N-66', 'score': 0.986473912937684}]
result = search.search('apricot kiwi lime coconut coconut apricot apple apple',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #441 checking search results for 'apricot kiwi lime coconut coconut apricot apple apple' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #441 checking search results for 'apricot kiwi lime coconut coconut apricot apple apple' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #442 checking search results for 'tomato pear pear peach pear' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html', 'title': 'N-3', 'score': 0.014517862793436746}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html', 'title': 'N-1', 'score': 0.013568570143095465}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html', 'title': 'N-0', 'score': 0.012455869330302472}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-6.html', 'title': 'N-6', 'score': 0.010211262598049326}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-4.html', 'title': 'N-4', 'score': 0.008747643433915257}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-12.html', 'title': 'N-12', 'score': 0.006933366357185256}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-15.html', 'title': 'N-15', 'score': 0.0064547298190873546}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-8.html', 'title': 'N-8', 'score': 0.006187749966071777}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-32.html', 'title': 'N-32', 'score': 0.006148352402154362}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-9.html', 'title': 'N-9', 'score': 0.00612370167774519}]
result = search.search('tomato pear pear peach pear',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #442 checking search results for 'tomato pear pear peach pear' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #442 checking search results for 'tomato pear pear peach pear' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #443 checking search results for 'kiwi lime blueberry cherry papaya kiwi cherry' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-600.html', 'title': 'N-600', 'score': 0.9963374756664615}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-351.html', 'title': 'N-351', 'score': 0.9937733528583998}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-466.html', 'title': 'N-466', 'score': 0.9930436322284593}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-192.html', 'title': 'N-192', 'score': 0.992788331013788}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-38.html', 'title': 'N-38', 'score': 0.9897344758515448}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-968.html', 'title': 'N-968', 'score': 0.9896863855430161}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-55.html', 'title': 'N-55', 'score': 0.9892944374278196}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-22.html', 'title': 'N-22', 'score': 0.9870995335756486}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-957.html', 'title': 'N-957', 'score': 0.9870904745456414}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-719.html', 'title': 'N-719', 'score': 0.9869195266980415}]
result = search.search('kiwi lime blueberry cherry papaya kiwi cherry',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #443 checking search results for 'kiwi lime blueberry cherry papaya kiwi cherry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #443 checking search results for 'kiwi lime blueberry cherry papaya kiwi cherry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #444 checking search results for 'pear lime orange orange lime peach kiwi apricot' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-238.html', 'title': 'N-238', 'score': 0.9932693581368416}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-471.html', 'title': 'N-471', 'score': 0.9913244781569152}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-211.html', 'title': 'N-211', 'score': 0.9907505920583712}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-999.html', 'title': 'N-999', 'score': 0.9898377904666769}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-19.html', 'title': 'N-19', 'score': 0.9886736402242016}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-745.html', 'title': 'N-745', 'score': 0.9883003242133195}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-219.html', 'title': 'N-219', 'score': 0.9876166705357189}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-844.html', 'title': 'N-844', 'score': 0.9862987692323556}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-755.html', 'title': 'N-755', 'score': 0.9861465564616495}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-839.html', 'title': 'N-839', 'score': 0.9842434683364744}]
result = search.search('pear lime orange orange lime peach kiwi apricot',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #444 checking search results for 'pear lime orange orange lime peach kiwi apricot' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #444 checking search results for 'pear lime orange orange lime peach kiwi apricot' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #445 checking search results for 'peach fig blueberry coconut orange peach apple' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-93.html', 'title': 'N-93', 'score': 0.9975802461637056}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-878.html', 'title': 'N-878', 'score': 0.9928664943750091}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-421.html', 'title': 'N-421', 'score': 0.989817937444709}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-437.html', 'title': 'N-437', 'score': 0.987844673857997}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-694.html', 'title': 'N-694', 'score': 0.987012843143029}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-127.html', 'title': 'N-127', 'score': 0.9864945661536599}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-246.html', 'title': 'N-246', 'score': 0.9862753700890005}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-608.html', 'title': 'N-608', 'score': 0.9859892578459089}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-902.html', 'title': 'N-902', 'score': 0.9857712723519442}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-501.html', 'title': 'N-501', 'score': 0.9856120729937919}]
result = search.search('peach fig blueberry coconut orange peach apple',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #445 checking search results for 'peach fig blueberry coconut orange peach apple' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #445 checking search results for 'peach fig blueberry coconut orange peach apple' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #446 checking search results for 'papaya blueberry papaya apple kiwi' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-14.html', 'title': 'N-14', 'score': 0.9998759963944953}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-833.html', 'title': 'N-833', 'score': 0.9995973997508906}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-308.html', 'title': 'N-308', 'score': 0.9994544561300943}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-589.html', 'title': 'N-589', 'score': 0.9980167000565032}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-501.html', 'title': 'N-501', 'score': 0.9979743174363801}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-551.html', 'title': 'N-551', 'score': 0.9977958655396567}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-902.html', 'title': 'N-902', 'score': 0.9975749284876188}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-660.html', 'title': 'N-660', 'score': 0.996620152502122}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-845.html', 'title': 'N-845', 'score': 0.9964742800669728}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-467.html', 'title': 'N-467', 'score': 0.9960673623068863}]
result = search.search('papaya blueberry papaya apple kiwi',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #446 checking search results for 'papaya blueberry papaya apple kiwi' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #446 checking search results for 'papaya blueberry papaya apple kiwi' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #447 checking search results for 'fig fig blueberry papaya apricot coconut apricot' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-470.html', 'title': 'N-470', 'score': 0.9984227191296092}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-150.html', 'title': 'N-150', 'score': 0.9976756442203731}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-22.html', 'title': 'N-22', 'score': 0.9932737250573922}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-375.html', 'title': 'N-375', 'score': 0.9931811484083988}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-521.html', 'title': 'N-521', 'score': 0.9920424268969668}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-596.html', 'title': 'N-596', 'score': 0.9911665929592964}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-485.html', 'title': 'N-485', 'score': 0.9910216876497911}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-676.html', 'title': 'N-676', 'score': 0.9905596723419694}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-260.html', 'title': 'N-260', 'score': 0.9886524790814601}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-835.html', 'title': 'N-835', 'score': 0.9880257918398981}]
result = search.search('fig fig blueberry papaya apricot coconut apricot',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #447 checking search results for 'fig fig blueberry papaya apricot coconut apricot' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #447 checking search results for 'fig fig blueberry papaya apricot coconut apricot' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #448 checking search results for 'fig fig apple tomato papaya banana kiwi fig' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-932.html', 'title': 'N-932', 'score': 0.9889262778879985}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-484.html', 'title': 'N-484', 'score': 0.9879599128600193}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-289.html', 'title': 'N-289', 'score': 0.9859054064436631}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-917.html', 'title': 'N-917', 'score': 0.9834770009015664}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-257.html', 'title': 'N-257', 'score': 0.9825486171166019}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-667.html', 'title': 'N-667', 'score': 0.9825137011903131}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-934.html', 'title': 'N-934', 'score': 0.9823682892451796}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-979.html', 'title': 'N-979', 'score': 0.9815615697156785}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-820.html', 'title': 'N-820', 'score': 0.9813952495221957}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-464.html', 'title': 'N-464', 'score': 0.9809749532424491}]
result = search.search('fig fig apple tomato papaya banana kiwi fig',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #448 checking search results for 'fig fig apple tomato papaya banana kiwi fig' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #448 checking search results for 'fig fig apple tomato papaya banana kiwi fig' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #449 checking search results for 'pear apricot coconut banana papaya coconut kiwi coconut' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-392.html', 'title': 'N-392', 'score': 0.9955202731583748}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-832.html', 'title': 'N-832', 'score': 0.9936284559798855}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-947.html', 'title': 'N-947', 'score': 0.9908018985887908}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-496.html', 'title': 'N-496', 'score': 0.9896731398695574}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-61.html', 'title': 'N-61', 'score': 0.9865156788493296}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-757.html', 'title': 'N-757', 'score': 0.9863298978357624}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-638.html', 'title': 'N-638', 'score': 0.9839959467507116}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-686.html', 'title': 'N-686', 'score': 0.9831491551134797}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-671.html', 'title': 'N-671', 'score': 0.9822464464493961}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-711.html', 'title': 'N-711', 'score': 0.9811853310333436}]
result = search.search('pear apricot coconut banana papaya coconut kiwi coconut',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #449 checking search results for 'pear apricot coconut banana papaya coconut kiwi coconut' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #449 checking search results for 'pear apricot coconut banana papaya coconut kiwi coconut' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #450 checking search results for 'pear peach peach peach apple blueberry' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-995.html', 'title': 'N-995', 'score': 0.9997894865945032}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-282.html', 'title': 'N-282', 'score': 0.9993495277094219}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-663.html', 'title': 'N-663', 'score': 0.9992060829475112}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-229.html', 'title': 'N-229', 'score': 0.998895440940847}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-246.html', 'title': 'N-246', 'score': 0.9962010997341312}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-948.html', 'title': 'N-948', 'score': 0.9937652771512354}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-437.html', 'title': 'N-437', 'score': 0.9936457538884311}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-523.html', 'title': 'N-523', 'score': 0.9908613577059221}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-134.html', 'title': 'N-134', 'score': 0.9885966656251235}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-608.html', 'title': 'N-608', 'score': 0.9876022585018435}]
result = search.search('pear peach peach peach apple blueberry',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #450 checking search results for 'pear peach peach peach apple blueberry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #450 checking search results for 'pear peach peach peach apple blueberry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #451 checking search results for 'papaya blueberry fig fig blueberry kiwi pear fig' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-991.html', 'title': 'N-991', 'score': 0.9971691661795083}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-792.html', 'title': 'N-792', 'score': 0.9900606133880032}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-202.html', 'title': 'N-202', 'score': 0.985888221280897}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-720.html', 'title': 'N-720', 'score': 0.9855852004845395}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-19.html', 'title': 'N-19', 'score': 0.9846005162331082}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-473.html', 'title': 'N-473', 'score': 0.9843623599695412}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-676.html', 'title': 'N-676', 'score': 0.9843491684428678}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-711.html', 'title': 'N-711', 'score': 0.9838617016861908}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-704.html', 'title': 'N-704', 'score': 0.9838578103957546}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-979.html', 'title': 'N-979', 'score': 0.9833308004314287}]
result = search.search('papaya blueberry fig fig blueberry kiwi pear fig',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #451 checking search results for 'papaya blueberry fig fig blueberry kiwi pear fig' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #451 checking search results for 'papaya blueberry fig fig blueberry kiwi pear fig' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #452 checking search results for 'banana banana apple peach fig kiwi banana tomato' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-796.html', 'title': 'N-796', 'score': 0.9929676474278244}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-43.html', 'title': 'N-43', 'score': 0.9906915772660493}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-264.html', 'title': 'N-264', 'score': 0.9904671786205952}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-261.html', 'title': 'N-261', 'score': 0.9833094525080642}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-737.html', 'title': 'N-737', 'score': 0.9817653411093816}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-356.html', 'title': 'N-356', 'score': 0.9800491571471348}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-750.html', 'title': 'N-750', 'score': 0.9748567183121633}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-896.html', 'title': 'N-896', 'score': 0.9742124283770949}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-707.html', 'title': 'N-707', 'score': 0.9716403493716091}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-729.html', 'title': 'N-729', 'score': 0.9692208744742233}]
result = search.search('banana banana apple peach fig kiwi banana tomato',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #452 checking search results for 'banana banana apple peach fig kiwi banana tomato' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #452 checking search results for 'banana banana apple peach fig kiwi banana tomato' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #453 checking search results for 'fig orange apricot orange peach apricot apple blueberry' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-446.html', 'title': 'N-446', 'score': 0.9934318244066633}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-723.html', 'title': 'N-723', 'score': 0.9931389042673098}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-378.html', 'title': 'N-378', 'score': 0.9878207216758261}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-892.html', 'title': 'N-892', 'score': 0.9872889713952783}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-250.html', 'title': 'N-250', 'score': 0.9864686169740906}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-900.html', 'title': 'N-900', 'score': 0.9852867488199182}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-9.html', 'title': 'N-9', 'score': 0.9850371348184328}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-20.html', 'title': 'N-20', 'score': 0.9824398027706036}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-721.html', 'title': 'N-721', 'score': 0.981581914639299}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-552.html', 'title': 'N-552', 'score': 0.9812925081056298}]
result = search.search('fig orange apricot orange peach apricot apple blueberry',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #453 checking search results for 'fig orange apricot orange peach apricot apple blueberry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #453 checking search results for 'fig orange apricot orange peach apricot apple blueberry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #454 checking search results for 'pear fig lime peach pear orange tomato' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-320.html', 'title': 'N-320', 'score': 0.9997757004140145}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-916.html', 'title': 'N-916', 'score': 0.9959103883317297}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-145.html', 'title': 'N-145', 'score': 0.9937607345283147}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-20.html', 'title': 'N-20', 'score': 0.9919552734057004}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-433.html', 'title': 'N-433', 'score': 0.9911490491121407}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-742.html', 'title': 'N-742', 'score': 0.9903708312321672}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-562.html', 'title': 'N-562', 'score': 0.990108623913249}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-814.html', 'title': 'N-814', 'score': 0.9900218651848888}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-106.html', 'title': 'N-106', 'score': 0.989790576175177}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-956.html', 'title': 'N-956', 'score': 0.9895649939963148}]
result = search.search('pear fig lime peach pear orange tomato',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #454 checking search results for 'pear fig lime peach pear orange tomato' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #454 checking search results for 'pear fig lime peach pear orange tomato' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #455 checking search results for 'orange banana lime orange kiwi papaya' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-61.html', 'title': 'N-61', 'score': 0.9998160826236256}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-126.html', 'title': 'N-126', 'score': 0.9996404358130574}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-804.html', 'title': 'N-804', 'score': 0.9974757110648078}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-596.html', 'title': 'N-596', 'score': 0.9973052402238191}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-311.html', 'title': 'N-311', 'score': 0.996208988762644}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-913.html', 'title': 'N-913', 'score': 0.994178933201861}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-67.html', 'title': 'N-67', 'score': 0.9940418295116771}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-267.html', 'title': 'N-267', 'score': 0.9931534756547403}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-286.html', 'title': 'N-286', 'score': 0.9929570580433783}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-314.html', 'title': 'N-314', 'score': 0.9919121051032223}]
result = search.search('orange banana lime orange kiwi papaya',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #455 checking search results for 'orange banana lime orange kiwi papaya' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #455 checking search results for 'orange banana lime orange kiwi papaya' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #456 checking search results for 'coconut tomato orange pear orange blueberry cherry' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html', 'title': 'N-3', 'score': 0.017267061962695125}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-12.html', 'title': 'N-12', 'score': 0.01723700530382519}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html', 'title': 'N-1', 'score': 0.014087529373882983}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html', 'title': 'N-0', 'score': 0.013914108458477337}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-15.html', 'title': 'N-15', 'score': 0.007814272028405104}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-6.html', 'title': 'N-6', 'score': 0.006625362996580971}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-8.html', 'title': 'N-8', 'score': 0.006175552372902942}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-4.html', 'title': 'N-4', 'score': 0.006131072167190932}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-32.html', 'title': 'N-32', 'score': 0.006096271731886918}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-9.html', 'title': 'N-9', 'score': 0.0060566468149557805}]
result = search.search('coconut tomato orange pear orange blueberry cherry',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #456 checking search results for 'coconut tomato orange pear orange blueberry cherry' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #456 checking search results for 'coconut tomato orange pear orange blueberry cherry' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #457 checking search results for 'banana pear fig pear orange cherry fig' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-423.html', 'title': 'N-423', 'score': 0.9998966342083352}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-586.html', 'title': 'N-586', 'score': 0.9942215449565621}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-251.html', 'title': 'N-251', 'score': 0.9931015105242946}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-393.html', 'title': 'N-393', 'score': 0.9929189014200402}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-177.html', 'title': 'N-177', 'score': 0.9926875138144203}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-899.html', 'title': 'N-899', 'score': 0.9918944539798259}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-813.html', 'title': 'N-813', 'score': 0.991718796911552}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-728.html', 'title': 'N-728', 'score': 0.991443202094702}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-544.html', 'title': 'N-544', 'score': 0.9907092490646996}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-226.html', 'title': 'N-226', 'score': 0.9901002479986669}]
result = search.search('banana pear fig pear orange cherry fig',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #457 checking search results for 'banana pear fig pear orange cherry fig' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #457 checking search results for 'banana pear fig pear orange cherry fig' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #458 checking search results for 'cherry pear orange fig lime fig fig' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-711.html', 'title': 'N-711', 'score': 0.9986937204833227}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-979.html', 'title': 'N-979', 'score': 0.9971018961792177}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-991.html', 'title': 'N-991', 'score': 0.9936390827498676}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-792.html', 'title': 'N-792', 'score': 0.9920603350514151}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-875.html', 'title': 'N-875', 'score': 0.9906212401047058}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-455.html', 'title': 'N-455', 'score': 0.98953296970691}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-720.html', 'title': 'N-720', 'score': 0.9880217861420169}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-924.html', 'title': 'N-924', 'score': 0.9879405408651519}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-674.html', 'title': 'N-674', 'score': 0.987066258842972}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-595.html', 'title': 'N-595', 'score': 0.9866752017265809}]
result = search.search('cherry pear orange fig lime fig fig',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #458 checking search results for 'cherry pear orange fig lime fig fig' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #458 checking search results for 'cherry pear orange fig lime fig fig' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #459 checking search results for 'peach apple banana orange fig pear' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-662.html', 'title': 'N-662', 'score': 0.9957686194097691}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-154.html', 'title': 'N-154', 'score': 0.9943264808009902}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-967.html', 'title': 'N-967', 'score': 0.9925090483530574}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-359.html', 'title': 'N-359', 'score': 0.9918065394757771}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-224.html', 'title': 'N-224', 'score': 0.9911118151501022}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-429.html', 'title': 'N-429', 'score': 0.9908776360484264}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-258.html', 'title': 'N-258', 'score': 0.9901881859883183}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-811.html', 'title': 'N-811', 'score': 0.9898556060904175}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-647.html', 'title': 'N-647', 'score': 0.9897971681219471}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-461.html', 'title': 'N-461', 'score': 0.9894871201785365}]
result = search.search('peach apple banana orange fig pear',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #459 checking search results for 'peach apple banana orange fig pear' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #459 checking search results for 'peach apple banana orange fig pear' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #460 checking search results for 'lime apricot apple coconut cherry banana fig cherry' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-456.html', 'title': 'N-456', 'score': 0.9887216771888904}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-313.html', 'title': 'N-313', 'score': 0.98838556571018}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-481.html', 'title': 'N-481', 'score': 0.9862177862377116}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-742.html', 'title': 'N-742', 'score': 0.9847081348656881}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-754.html', 'title': 'N-754', 'score': 0.9842526341861971}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-738.html', 'title': 'N-738', 'score': 0.983824003379797}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-340.html', 'title': 'N-340', 'score': 0.9813118982255663}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-165.html', 'title': 'N-165', 'score': 0.9809316268877328}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-530.html', 'title': 'N-530', 'score': 0.9809182597362905}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-316.html', 'title': 'N-316', 'score': 0.9805776883666496}]
result = search.search('lime apricot apple coconut cherry banana fig cherry',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #460 checking search results for 'lime apricot apple coconut cherry banana fig cherry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #460 checking search results for 'lime apricot apple coconut cherry banana fig cherry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #461 checking search results for 'blueberry kiwi kiwi orange peach orange pear' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-162.html', 'title': 'N-162', 'score': 0.9915339098734145}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-271.html', 'title': 'N-271', 'score': 0.9901224443873419}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-216.html', 'title': 'N-216', 'score': 0.9897724217752267}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-155.html', 'title': 'N-155', 'score': 0.9897463714170844}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-450.html', 'title': 'N-450', 'score': 0.9897043414023199}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-83.html', 'title': 'N-83', 'score': 0.9891285347493547}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-587.html', 'title': 'N-587', 'score': 0.9881057307728424}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-918.html', 'title': 'N-918', 'score': 0.9877514148169969}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-729.html', 'title': 'N-729', 'score': 0.9874683823714702}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-590.html', 'title': 'N-590', 'score': 0.9865680085294254}]
result = search.search('blueberry kiwi kiwi orange peach orange pear',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #461 checking search results for 'blueberry kiwi kiwi orange peach orange pear' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #461 checking search results for 'blueberry kiwi kiwi orange peach orange pear' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #462 checking search results for 'blueberry blueberry papaya lime pear blueberry tomato' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-340.html', 'title': 'N-340', 'score': 0.9986051382110135}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-473.html', 'title': 'N-473', 'score': 0.9954528147858235}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-57.html', 'title': 'N-57', 'score': 0.9941343719002276}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-979.html', 'title': 'N-979', 'score': 0.9934596336570053}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-675.html', 'title': 'N-675', 'score': 0.9930838684591901}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-798.html', 'title': 'N-798', 'score': 0.9928532320978031}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-373.html', 'title': 'N-373', 'score': 0.9923371192651517}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-681.html', 'title': 'N-681', 'score': 0.99076808733137}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-15.html', 'title': 'N-15', 'score': 0.9906446882433896}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-486.html', 'title': 'N-486', 'score': 0.9904889582010867}]
result = search.search('blueberry blueberry papaya lime pear blueberry tomato',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #462 checking search results for 'blueberry blueberry papaya lime pear blueberry tomato' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #462 checking search results for 'blueberry blueberry papaya lime pear blueberry tomato' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


output.close()
success_output.close()







output.close()
success_output.close()
