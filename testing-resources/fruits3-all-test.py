
import testingtools
import crawler
import searchdata
import search

#Performing crawl starting at seed http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html
crawler.crawl('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html')


output = open('fruits3-all-outgoing-failed.txt', 'w')
success_output = open('fruits3-all-outgoing-passed.txt', 'w')

#Test #0 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-575.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-231.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-575.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #0 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-575.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #0 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-575.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #1 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-205.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-252.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-916.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-231.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-305.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-415.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-205.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #1 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-205.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #1 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-205.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #2 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-430.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-200.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-430.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #2 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-430.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #2 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-430.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #3 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-738.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-3.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-9.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-738.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #3 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-738.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #3 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-738.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #4 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-982.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-6.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-110.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-847.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-982.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #4 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-982.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #4 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-982.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #5 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-117.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-6.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-117.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #5 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-117.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #5 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-117.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #6 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-883.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-11.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-352.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-918.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-883.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #6 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-883.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #6 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-883.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #7 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-392.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-547.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-887.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-193.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-392.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #7 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-392.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #7 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-392.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #8 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-111.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-65.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-111.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #8 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-111.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #8 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-111.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #9 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-267.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-41.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-734.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-872.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-267.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #9 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-267.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #9 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-267.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #10 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-449.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-125.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-823.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-54.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-449.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #10 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-449.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #10 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-449.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #11 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-986.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-25.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-986.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #11 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-986.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #11 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-986.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #12 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-668.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-5.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-668.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #12 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-668.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #12 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-668.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #13 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-487.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-25.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-40.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-884.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-505.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-487.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #13 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-487.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #13 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-487.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #14 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-793.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-37.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-511.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-732.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-867.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-793.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #14 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-793.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #14 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-793.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #15 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-567.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-2.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-537.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-567.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #15 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-567.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #15 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-567.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #16 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-152.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-7.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-152.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #16 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-152.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #16 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-152.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #17 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-752.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-34.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-69.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-394.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-752.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #17 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-752.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #17 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-752.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #18 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-671.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-377.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-671.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #18 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-671.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #18 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-671.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #19 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-854.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-92.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-447.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-854.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #19 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-854.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #19 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-854.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #20 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-817.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-791.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-817.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #20 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-817.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #20 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-817.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #21 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-546.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-4.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-546.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #21 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-546.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #21 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-546.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #22 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-407.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-110.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-453.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-651.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-129.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-719.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-407.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #22 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-407.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #22 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-407.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #23 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-9.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-30.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-53.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-96.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-310.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-389.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-486.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-523.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-738.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-765.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-25.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-28.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-36.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-84.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-160.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-222.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-238.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-309.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-908.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-978.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-9.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #23 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-9.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #23 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-9.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #24 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-951.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-4.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-68.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-72.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-951.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #24 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-951.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #24 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-951.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #25 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-182.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-180.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-182.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #25 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-182.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #25 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-182.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #26 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-224.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-25.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-224.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #26 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-224.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #26 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-224.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #27 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-913.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-23.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-6.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-913.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #27 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-913.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #27 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-913.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #28 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-940.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-940.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #28 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-940.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #28 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-940.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #29 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-508.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-419.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-508.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #29 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-508.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #29 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-508.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #30 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-293.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-4.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-151.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-335.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-520.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-181.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-293.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #30 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-293.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #30 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-293.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #31 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-456.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-316.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-333.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-611.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-621.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-456.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #31 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-456.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #31 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-456.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #32 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-79.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-7.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-60.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-144.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-170.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-761.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-770.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-318.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-423.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-969.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-79.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #32 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-79.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #32 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-79.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #33 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-440.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-25.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-440.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #33 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-440.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #33 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-440.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #34 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-1.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-781.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-15.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-90.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-207.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-1.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #34 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-1.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #34 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-1.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #35 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-101.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-16.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-63.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-101.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #35 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-101.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #35 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-101.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #36 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-635.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-10.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-635.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #36 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-635.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #36 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-635.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #37 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-148.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-114.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-148.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #37 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-148.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #37 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-148.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #38 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-706.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-901.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-38.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-552.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-962.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-706.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #38 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-706.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #38 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-706.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #39 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-173.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-60.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-193.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-446.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-141.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-173.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #39 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-173.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #39 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-173.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #40 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-767.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-6.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-767.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #40 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-767.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #40 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-767.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #41 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-329.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-7.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-239.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-352.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-64.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-555.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-329.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #41 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-329.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #41 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-329.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #42 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-126.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-69.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-552.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-126.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #42 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-126.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #42 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-126.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #43 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-322.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-178.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-322.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #43 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-322.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #43 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-322.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #44 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-129.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-407.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-6.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-212.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-731.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-941.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-129.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #44 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-129.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #44 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-129.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #45 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-628.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-611.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-309.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-521.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-976.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-628.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #45 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-628.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #45 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-628.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #46 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-935.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-268.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-15.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-935.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #46 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-935.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #46 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-935.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #47 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-568.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-203.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-395.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-568.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #47 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-568.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #47 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-568.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #48 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-980.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-677.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-720.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-980.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #48 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-980.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #48 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-980.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #49 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-376.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-232.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-388.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-930.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-376.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #49 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-376.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #49 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-376.html\n\n')
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









output = open('fruits3-all-incoming-failed.txt', 'w')
success_output = open('fruits3-all-incoming-passed.txt', 'w')

#Test #51 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-459.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-4.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-947.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-459.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #51 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-459.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #51 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-459.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #52 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-41.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-6.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-90.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-512.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-211.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-43.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-338.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-137.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-113.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-267.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-535.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-490.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-166.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-608.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-551.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-112.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-78.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-529.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-602.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-640.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-890.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-41.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #52 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-41.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #52 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-41.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #53 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-717.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-513.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-198.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-717.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #53 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-717.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #53 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-717.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #54 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-434.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-25.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-677.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-902.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-658.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-862.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-434.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #54 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-434.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #54 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-434.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #55 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-374.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-2.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-5.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-374.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #55 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-374.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #55 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-374.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #56 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-532.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-232.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-21.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-303.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-532.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #56 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-532.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #56 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-532.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #57 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-617.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-497.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-81.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-73.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-617.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #57 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-617.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #57 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-617.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #58 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-67.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-5.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-67.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #58 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-67.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #58 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-67.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #59 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-971.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-341.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-971.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #59 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-971.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #59 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-971.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #60 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-861.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-5.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-308.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-861.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #60 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-861.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #60 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-861.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #61 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-485.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-65.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-485.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #61 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-485.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #61 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-485.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #62 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-750.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-3.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-406.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-303.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-957.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-750.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #62 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-750.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #62 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-750.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #63 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-626.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-6.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-626.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #63 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-626.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #63 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-626.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #64 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-349.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-424.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-99.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-349.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #64 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-349.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #64 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-349.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #65 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-566.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-5.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-234.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-566.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #65 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-566.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #65 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-566.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #66 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-303.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-38.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-712.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-532.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-750.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-303.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #66 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-303.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #66 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-303.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #67 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-816.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-16.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-78.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-909.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-816.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #67 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-816.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #67 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-816.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #68 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-657.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-333.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-657.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #68 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-657.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #68 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-657.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #69 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-679.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-118.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-726.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-679.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #69 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-679.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #69 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-679.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #70 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-610.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-137.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-610.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #70 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-610.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #70 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-610.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #71 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-561.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-114.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-561.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #71 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-561.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #71 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-561.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #72 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-746.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-258.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-746.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #72 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-746.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #72 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-746.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #73 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-665.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-247.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-700.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-665.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #73 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-665.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #73 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-665.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #74 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-965.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-655.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-965.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #74 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-965.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #74 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-965.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #75 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-61.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-5.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-280.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-162.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-61.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #75 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-61.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #75 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-61.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #76 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-283.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-40.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-556.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-92.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-294.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-283.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #76 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-283.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #76 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-283.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #77 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-753.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-217.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-160.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-915.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-94.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-753.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #77 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-753.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #77 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-753.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #78 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-673.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-59.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-673.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #78 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-673.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #78 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-673.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #79 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-643.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-13.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-643.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #79 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-643.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #79 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-643.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #80 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-277.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-30.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-627.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-664.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-650.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-277.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #80 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-277.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #80 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-277.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #81 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-972.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-808.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-972.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #81 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-972.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #81 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-972.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #82 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-157.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-143.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-51.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-195.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-927.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-157.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #82 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-157.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #82 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-157.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #83 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-868.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-700.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-868.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #83 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-868.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #83 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-868.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #84 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-167.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-33.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-989.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-167.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #84 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-167.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #84 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-167.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #85 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-898.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-198.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-898.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #85 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-898.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #85 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-898.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #86 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-498.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-309.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-498.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #86 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-498.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #86 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-498.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #87 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-916.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-205.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-504.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-81.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-916.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #87 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-916.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #87 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-916.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #88 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-48.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-91.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-311.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-453.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-40.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-174.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-275.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-29.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-48.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #88 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-48.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #88 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-48.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #89 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-289.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-219.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-289.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #89 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-289.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #89 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-289.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #90 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-961.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-845.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-961.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #90 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-961.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #90 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-961.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #91 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-10.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-7.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-435.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-563.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-241.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-326.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-175.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-306.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-274.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-69.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-822.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-478.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-923.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-118.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-288.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-410.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-571.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-203.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-43.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-995.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-791.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-747.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-273.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-792.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-238.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-97.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-364.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-420.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-577.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-120.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-139.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-142.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-146.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-275.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-635.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-794.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-857.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-229.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-358.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-803.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-844.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-903.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-10.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #91 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-10.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #91 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-10.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #92 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-930.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-376.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-930.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #92 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-930.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #92 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-930.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #93 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-866.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-539.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-866.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #93 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-866.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #93 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-866.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #94 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-12.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-4.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-332.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-25.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-326.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-143.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-325.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-692.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-147.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-583.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-47.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-55.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-714.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-900.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-932.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-954.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-12.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #94 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-12.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #94 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-12.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #95 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-720.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-5.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-51.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-99.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-980.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-720.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #95 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-720.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #95 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-720.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #96 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-443.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-236.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-725.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-855.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-162.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-681.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-870.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-443.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #96 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-443.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #96 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-443.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #97 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-675.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-71.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-682.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-675.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #97 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-675.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #97 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-675.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #98 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-103.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-6.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-97.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-278.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-103.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #98 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-103.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #98 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-103.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #99 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-95.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-81.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-95.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #99 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-95.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #99 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-95.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #100 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-550.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-241.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-876.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-525.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-550.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #100 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-550.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #100 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-550.html\n\n')
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









output = open('fruits3-all-pagerank-failed.txt', 'w')
success_output = open('fruits3-all-pagerank-passed.txt', 'w')

#Test #102 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-841.html
expected = 0.0006169618006254619
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-841.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #102 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-841.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #102 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-841.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #103 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-714.html
expected = 0.000621636818767281
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-714.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #103 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-714.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #103 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-714.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #104 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-761.html
expected = 0.0011776235271562584
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-761.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #104 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-761.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #104 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-761.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #105 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-143.html
expected = 0.005387517881743759
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-143.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #105 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-143.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #105 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-143.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #106 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-410.html
expected = 0.0011622164369404272
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-410.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #106 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-410.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #106 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-410.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #107 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-570.html
expected = 0.00036436504230668237
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-570.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #107 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-570.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #107 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-570.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #108 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-793.html
expected = 0.0012125834941151127
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-793.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #108 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-793.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #108 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-793.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #109 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-771.html
expected = 0.0006571799349994139
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-771.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #109 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-771.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #109 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-771.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #110 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-930.html
expected = 0.0004075884017553431
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-930.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #110 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-930.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #110 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-930.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #111 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-916.html
expected = 0.0009486585105563897
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-916.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #111 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-916.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #111 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-916.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #112 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-262.html
expected = 0.0006426829800631401
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-262.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #112 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-262.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #112 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-262.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #113 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-954.html
expected = 0.0003598702139167251
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-954.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #113 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-954.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #113 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-954.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #114 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-113.html
expected = 0.0008609976531906747
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-113.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #114 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-113.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #114 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-113.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #115 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-749.html
expected = 0.0006208597682303282
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-749.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #115 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-749.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #115 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-749.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #116 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-63.html
expected = 0.002495378492294464
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-63.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #116 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-63.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #116 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-63.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #117 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-694.html
expected = 0.0007278731815320664
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-694.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #117 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-694.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #117 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-694.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #118 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-478.html
expected = 0.0012046342790292366
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-478.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #118 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-478.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #118 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-478.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #119 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-151.html
expected = 0.0006524772395176779
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-151.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #119 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-151.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #119 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-151.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #120 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-498.html
expected = 0.00036436504230668237
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-498.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #120 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-498.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #120 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-498.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #121 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-575.html
expected = 0.0003928676700295915
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-575.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #121 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-575.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #121 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-575.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #122 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-114.html
expected = 0.0031936570614710244
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-114.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #122 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-114.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #122 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-114.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #123 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-263.html
expected = 0.0017436270803088108
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-263.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #123 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-263.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #123 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-263.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #124 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-585.html
expected = 0.00038271141708291274
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-585.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #124 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-585.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #124 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-585.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #125 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-423.html
expected = 0.0006328842775615634
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-423.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #125 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-423.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #125 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-423.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #126 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-213.html
expected = 0.0004419685283497025
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-213.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #126 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-213.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #126 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-213.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #127 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-54.html
expected = 0.0018109676135891625
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-54.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #127 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-54.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #127 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-54.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #128 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-983.html
expected = 0.00044018557743654037
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-983.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #128 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-983.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #128 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-983.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #129 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-28.html
expected = 0.0006503067814321614
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-28.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #129 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-28.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #129 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-28.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #130 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-180.html
expected = 0.0022852105721470704
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-180.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #130 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-180.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #130 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-180.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #131 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-249.html
expected = 0.0003650058299508677
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-249.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #131 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-249.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #131 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-249.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #132 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-146.html
expected = 0.0003527449742692324
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-146.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #132 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-146.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #132 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-146.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #133 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-103.html
expected = 0.0008957187384839581
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-103.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #133 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-103.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #133 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-103.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #134 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-649.html
expected = 0.00036363171183258805
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-649.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #134 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-649.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #134 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-649.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #135 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-605.html
expected = 0.00034863440432348014
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-605.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #135 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-605.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #135 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-605.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #136 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-542.html
expected = 0.0010305622487162902
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-542.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #136 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-542.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #136 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-542.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #137 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-528.html
expected = 0.0003546949791166664
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-528.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #137 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-528.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #137 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-528.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #138 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-239.html
expected = 0.0009058300046973127
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-239.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #138 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-239.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #138 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-239.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #139 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-303.html
expected = 0.0011607056194778938
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-303.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #139 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-303.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #139 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-303.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #140 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-980.html
expected = 0.0006200654254945889
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-980.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #140 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-980.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #140 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-980.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #141 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-795.html
expected = 0.000412783932733821
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-795.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #141 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-795.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #141 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-795.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #142 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-18.html
expected = 0.0013798188568625257
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-18.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #142 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-18.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #142 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-18.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #143 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-345.html
expected = 0.00037747146593684254
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-345.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #143 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-345.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #143 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-345.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #144 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-949.html
expected = 0.0003548677054033544
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-949.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #144 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-949.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #144 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-949.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #145 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-614.html
expected = 0.0003776635005797719
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-614.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #145 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-614.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #145 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-614.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #146 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-232.html
expected = 0.004067704157110919
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-232.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #146 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-232.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #146 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-232.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #147 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-268.html
expected = 0.001016092013720277
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-268.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #147 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-268.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #147 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-268.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #148 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-942.html
expected = 0.0004036212459905852
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-942.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #148 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-942.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #148 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-942.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #149 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-257.html
expected = 0.0003784444439070059
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-257.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #149 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-257.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #149 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-257.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #150 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-339.html
expected = 0.0003659017776968428
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-339.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #150 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-339.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #150 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-339.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #151 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-632.html
expected = 0.0006261813135875305
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-632.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #151 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-632.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #151 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-632.html\n\n')
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









output = open('fruits3-all-idf-failed.txt', 'w')
success_output = open('fruits3-all-idf-passed.txt', 'w')

#Test #153 checking IDF for word orange
expected = 0.16812275880832706
result = searchdata.get_idf('orange')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #153 checking IDF for word orange\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #153 checking IDF for word orange\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #154 checking IDF for word coconut
expected = 0.18114943910456646
result = searchdata.get_idf('coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #154 checking IDF for word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #154 checking IDF for word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #155 checking IDF for word cherry
expected = 0.1600404125104682
result = searchdata.get_idf('cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #155 checking IDF for word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #155 checking IDF for word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #156 checking IDF for word papaya
expected = 0.1762506396917273
result = searchdata.get_idf('papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #156 checking IDF for word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #156 checking IDF for word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #157 checking IDF for word peach
expected = 0.1600404125104682
result = searchdata.get_idf('peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #157 checking IDF for word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #157 checking IDF for word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #158 checking IDF for word pear
expected = 0.17462139610706884
result = searchdata.get_idf('pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #158 checking IDF for word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #158 checking IDF for word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #159 checking IDF for word banana
expected = 0.15842936260448298
result = searchdata.get_idf('banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #159 checking IDF for word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #159 checking IDF for word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #160 checking IDF for word blueberry
expected = 0.17136841831198113
result = searchdata.get_idf('blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #160 checking IDF for word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #160 checking IDF for word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #161 checking IDF for word kiwi
expected = 0.15842936260448298
result = searchdata.get_idf('kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #161 checking IDF for word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #161 checking IDF for word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #162 checking IDF for word lime
expected = 0.20922796213800016
result = searchdata.get_idf('lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #162 checking IDF for word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #162 checking IDF for word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #163 checking IDF for word fig
expected = 0.16650266314016507
result = searchdata.get_idf('fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #163 checking IDF for word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #163 checking IDF for word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #164 checking IDF for word apple
expected = 0.1729939903610231
result = searchdata.get_idf('apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #164 checking IDF for word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #164 checking IDF for word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #165 checking IDF for word apricot
expected = 0.16650266314016507
result = searchdata.get_idf('apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #165 checking IDF for word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #165 checking IDF for word apricot\n\n')
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









output = open('fruits3-all-tf-failed.txt', 'w')
success_output = open('fruits3-all-tf-passed.txt', 'w')

#Test #167 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-721.html and word peach
expected = 0.0625
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-721.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #167 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-721.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #167 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-721.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #168 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-721.html and word orange
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-721.html','orange')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #168 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-721.html and word orange\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #168 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-721.html and word orange\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #169 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-721.html and word lime
expected = 0.125
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-721.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #169 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-721.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #169 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-721.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #170 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-721.html and word apple
expected = 0.0625
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-721.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #170 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-721.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #170 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-721.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #171 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-721.html and word apricot
expected = 0.0625
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-721.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #171 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-721.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #171 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-721.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #172 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-721.html and word fig
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-721.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #172 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-721.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #172 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-721.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #173 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-721.html and word blueberry
expected = 0.1875
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-721.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #173 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-721.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #173 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-721.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #174 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-721.html and word cherry
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-721.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #174 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-721.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #174 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-721.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #175 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-721.html and word pear
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-721.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #175 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-721.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #175 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-721.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #176 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-721.html and word kiwi
expected = 0.125
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-721.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #176 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-721.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #176 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-721.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #177 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-721.html and word tomato
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-721.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #177 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-721.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #177 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-721.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #178 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-320.html and word peach
expected = 0.02857142857142857
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-320.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #178 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-320.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #178 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-320.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #179 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-320.html and word orange
expected = 0.05714285714285714
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-320.html','orange')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #179 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-320.html and word orange\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #179 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-320.html and word orange\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #180 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-320.html and word lime
expected = 0.08571428571428572
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-320.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #180 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-320.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #180 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-320.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #181 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-320.html and word apple
expected = 0.11428571428571428
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-320.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #181 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-320.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #181 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-320.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #182 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-320.html and word apricot
expected = 0.14285714285714285
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-320.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #182 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-320.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #182 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-320.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #183 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-320.html and word fig
expected = 0.05714285714285714
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-320.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #183 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-320.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #183 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-320.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #184 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-320.html and word blueberry
expected = 0.02857142857142857
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-320.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #184 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-320.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #184 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-320.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #185 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-320.html and word cherry
expected = 0.05714285714285714
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-320.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #185 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-320.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #185 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-320.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #186 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-320.html and word pear
expected = 0.05714285714285714
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-320.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #186 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-320.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #186 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-320.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #187 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-320.html and word kiwi
expected = 0.11428571428571428
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-320.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #187 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-320.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #187 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-320.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #188 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-320.html and word tomato
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-320.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #188 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-320.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #188 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-320.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #189 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-618.html and word peach
expected = 0.018867924528301886
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-618.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #189 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-618.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #189 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-618.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #190 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-618.html and word orange
expected = 0.11320754716981132
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-618.html','orange')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #190 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-618.html and word orange\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #190 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-618.html and word orange\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #191 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-618.html and word lime
expected = 0.09433962264150944
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-618.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #191 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-618.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #191 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-618.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #192 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-618.html and word apple
expected = 0.018867924528301886
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-618.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #192 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-618.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #192 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-618.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #193 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-618.html and word apricot
expected = 0.09433962264150944
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-618.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #193 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-618.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #193 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-618.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #194 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-618.html and word fig
expected = 0.05660377358490566
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-618.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #194 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-618.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #194 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-618.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #195 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-618.html and word blueberry
expected = 0.09433962264150944
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-618.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #195 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-618.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #195 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-618.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #196 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-618.html and word cherry
expected = 0.07547169811320754
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-618.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #196 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-618.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #196 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-618.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #197 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-618.html and word pear
expected = 0.05660377358490566
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-618.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #197 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-618.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #197 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-618.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #198 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-618.html and word kiwi
expected = 0.03773584905660377
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-618.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #198 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-618.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #198 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-618.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #199 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-618.html and word tomato
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-618.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #199 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-618.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #199 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-618.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #200 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-491.html and word peach
expected = 0.06315789473684211
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-491.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #200 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-491.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #200 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-491.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #201 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-491.html and word orange
expected = 0.10526315789473684
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-491.html','orange')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #201 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-491.html and word orange\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #201 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-491.html and word orange\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #202 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-491.html and word lime
expected = 0.06315789473684211
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-491.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #202 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-491.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #202 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-491.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #203 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-491.html and word apple
expected = 0.08421052631578947
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-491.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #203 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-491.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #203 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-491.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #204 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-491.html and word apricot
expected = 0.05263157894736842
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-491.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #204 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-491.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #204 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-491.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #205 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-491.html and word fig
expected = 0.05263157894736842
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-491.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #205 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-491.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #205 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-491.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #206 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-491.html and word blueberry
expected = 0.14736842105263157
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-491.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #206 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-491.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #206 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-491.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #207 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-491.html and word cherry
expected = 0.14736842105263157
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-491.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #207 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-491.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #207 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-491.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #208 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-491.html and word pear
expected = 0.08421052631578947
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-491.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #208 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-491.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #208 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-491.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #209 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-491.html and word kiwi
expected = 0.07368421052631578
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-491.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #209 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-491.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #209 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-491.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #210 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-491.html and word tomato
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-491.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #210 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-491.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #210 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-491.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #211 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-113.html and word peach
expected = 0.08333333333333333
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-113.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #211 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-113.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #211 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-113.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #212 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-113.html and word orange
expected = 0.05555555555555555
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-113.html','orange')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #212 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-113.html and word orange\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #212 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-113.html and word orange\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #213 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-113.html and word lime
expected = 0.041666666666666664
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-113.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #213 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-113.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #213 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-113.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #214 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-113.html and word apple
expected = 0.09722222222222222
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-113.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #214 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-113.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #214 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-113.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #215 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-113.html and word apricot
expected = 0.05555555555555555
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-113.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #215 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-113.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #215 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-113.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #216 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-113.html and word fig
expected = 0.05555555555555555
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-113.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #216 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-113.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #216 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-113.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #217 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-113.html and word blueberry
expected = 0.05555555555555555
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-113.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #217 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-113.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #217 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-113.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #218 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-113.html and word cherry
expected = 0.05555555555555555
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-113.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #218 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-113.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #218 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-113.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #219 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-113.html and word pear
expected = 0.05555555555555555
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-113.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #219 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-113.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #219 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-113.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #220 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-113.html and word kiwi
expected = 0.08333333333333333
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-113.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #220 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-113.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #220 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-113.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #221 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-113.html and word tomato
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-113.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #221 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-113.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #221 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-113.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #222 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-801.html and word peach
expected = 0.06451612903225806
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-801.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #222 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-801.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #222 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-801.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #223 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-801.html and word orange
expected = 0.0967741935483871
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-801.html','orange')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #223 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-801.html and word orange\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #223 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-801.html and word orange\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #224 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-801.html and word lime
expected = 0.0967741935483871
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-801.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #224 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-801.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #224 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-801.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #225 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-801.html and word apple
expected = 0.12903225806451613
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-801.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #225 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-801.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #225 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-801.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #226 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-801.html and word apricot
expected = 0.12903225806451613
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-801.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #226 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-801.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #226 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-801.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #227 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-801.html and word fig
expected = 0.06451612903225806
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-801.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #227 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-801.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #227 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-801.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #228 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-801.html and word blueberry
expected = 0.06451612903225806
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-801.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #228 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-801.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #228 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-801.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #229 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-801.html and word cherry
expected = 0.06451612903225806
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-801.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #229 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-801.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #229 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-801.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #230 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-801.html and word pear
expected = 0.0967741935483871
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-801.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #230 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-801.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #230 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-801.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #231 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-801.html and word kiwi
expected = 0.06451612903225806
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-801.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #231 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-801.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #231 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-801.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #232 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-801.html and word tomato
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-801.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #232 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-801.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #232 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-801.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #233 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-224.html and word peach
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-224.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #233 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-224.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #233 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-224.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #234 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-224.html and word orange
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-224.html','orange')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #234 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-224.html and word orange\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #234 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-224.html and word orange\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #235 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-224.html and word lime
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-224.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #235 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-224.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #235 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-224.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #236 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-224.html and word apple
expected = 0.14285714285714285
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-224.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #236 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-224.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #236 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-224.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #237 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-224.html and word apricot
expected = 0.14285714285714285
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-224.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #237 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-224.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #237 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-224.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #238 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-224.html and word fig
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-224.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #238 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-224.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #238 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-224.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #239 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-224.html and word blueberry
expected = 0.14285714285714285
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-224.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #239 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-224.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #239 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-224.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #240 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-224.html and word cherry
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-224.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #240 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-224.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #240 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-224.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #241 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-224.html and word pear
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-224.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #241 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-224.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #241 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-224.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #242 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-224.html and word kiwi
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-224.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #242 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-224.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #242 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-224.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #243 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-224.html and word tomato
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-224.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #243 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-224.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #243 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-224.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #244 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-503.html and word peach
expected = 0.1282051282051282
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-503.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #244 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-503.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #244 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-503.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #245 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-503.html and word orange
expected = 0.10256410256410256
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-503.html','orange')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #245 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-503.html and word orange\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #245 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-503.html and word orange\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #246 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-503.html and word lime
expected = 0.02564102564102564
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-503.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #246 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-503.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #246 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-503.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #247 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-503.html and word apple
expected = 0.05128205128205128
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-503.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #247 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-503.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #247 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-503.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #248 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-503.html and word apricot
expected = 0.20512820512820512
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-503.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #248 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-503.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #248 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-503.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #249 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-503.html and word fig
expected = 0.05128205128205128
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-503.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #249 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-503.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #249 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-503.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #250 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-503.html and word blueberry
expected = 0.05128205128205128
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-503.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #250 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-503.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #250 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-503.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #251 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-503.html and word cherry
expected = 0.05128205128205128
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-503.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #251 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-503.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #251 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-503.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #252 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-503.html and word pear
expected = 0.02564102564102564
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-503.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #252 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-503.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #252 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-503.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #253 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-503.html and word kiwi
expected = 0.05128205128205128
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-503.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #253 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-503.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #253 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-503.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #254 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-503.html and word tomato
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-503.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #254 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-503.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #254 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-503.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #255 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-225.html and word peach
expected = 0.05952380952380952
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-225.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #255 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-225.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #255 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-225.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #256 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-225.html and word orange
expected = 0.047619047619047616
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-225.html','orange')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #256 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-225.html and word orange\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #256 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-225.html and word orange\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #257 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-225.html and word lime
expected = 0.05952380952380952
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-225.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #257 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-225.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #257 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-225.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #258 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-225.html and word apple
expected = 0.07142857142857142
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-225.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #258 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-225.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #258 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-225.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #259 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-225.html and word apricot
expected = 0.10714285714285714
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-225.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #259 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-225.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #259 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-225.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #260 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-225.html and word fig
expected = 0.11904761904761904
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-225.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #260 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-225.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #260 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-225.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #261 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-225.html and word blueberry
expected = 0.07142857142857142
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-225.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #261 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-225.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #261 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-225.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #262 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-225.html and word cherry
expected = 0.08333333333333333
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-225.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #262 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-225.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #262 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-225.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #263 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-225.html and word pear
expected = 0.13095238095238096
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-225.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #263 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-225.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #263 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-225.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #264 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-225.html and word kiwi
expected = 0.09523809523809523
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-225.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #264 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-225.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #264 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-225.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #265 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-225.html and word tomato
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-225.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #265 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-225.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #265 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-225.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #266 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-465.html and word peach
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-465.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #266 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-465.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #266 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-465.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #267 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-465.html and word orange
expected = 0.045454545454545456
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-465.html','orange')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #267 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-465.html and word orange\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #267 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-465.html and word orange\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #268 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-465.html and word lime
expected = 0.045454545454545456
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-465.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #268 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-465.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #268 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-465.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #269 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-465.html and word apple
expected = 0.045454545454545456
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-465.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #269 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-465.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #269 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-465.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #270 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-465.html and word apricot
expected = 0.09090909090909091
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-465.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #270 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-465.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #270 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-465.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #271 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-465.html and word fig
expected = 0.09090909090909091
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-465.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #271 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-465.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #271 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-465.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #272 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-465.html and word blueberry
expected = 0.18181818181818182
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-465.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #272 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-465.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #272 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-465.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #273 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-465.html and word cherry
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-465.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #273 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-465.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #273 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-465.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #274 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-465.html and word pear
expected = 0.045454545454545456
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-465.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #274 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-465.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #274 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-465.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #275 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-465.html and word kiwi
expected = 0.13636363636363635
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-465.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #275 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-465.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #275 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-465.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #276 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-465.html and word tomato
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-465.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #276 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-465.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #276 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-465.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #277 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word peach
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #277 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #277 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #278 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word orange
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','orange')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #278 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word orange\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #278 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word orange\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #279 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word lime
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #279 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #279 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #280 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word apple
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #280 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #280 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word apple\n\n')
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


#Test #283 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word blueberry
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #283 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #283 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #284 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word cherry
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #284 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #284 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #285 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word pear
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #285 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #285 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #286 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word kiwi
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #286 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #286 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word kiwi\n\n')
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









output = open('fruits3-all-tfidf-failed.txt', 'w')
success_output = open('fruits3-all-tfidf-passed.txt', 'w')

#Test #288 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-506.html and word orange
expected = 0.02110459821158114
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-506.html','orange')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #288 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-506.html and word orange\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #288 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-506.html and word orange\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #289 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-506.html and word coconut
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-506.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #289 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-506.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #289 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-506.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #290 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-506.html and word pear
expected = 0.06075485298143729
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-506.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #290 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-506.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #290 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-506.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #291 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-506.html and word blueberry
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-506.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #291 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-506.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #291 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-506.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #292 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-506.html and word papaya
expected = 0.022124898268346908
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-506.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #292 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-506.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #292 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-506.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #293 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-506.html and word banana
expected = 0.019887777635724264
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-506.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #293 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-506.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #293 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-506.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #294 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-506.html and word apricot
expected = 0.02090122617329653
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-506.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #294 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-506.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #294 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-506.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #295 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-506.html and word peach
expected = 0.038571035662951315
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-506.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #295 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-506.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #295 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-506.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #296 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-506.html and word fig
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-506.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #296 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-506.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #296 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-506.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #297 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-506.html and word lime
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-506.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #297 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-506.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #297 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-506.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #298 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-506.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-506.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #298 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-506.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #298 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-506.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #299 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-248.html and word orange
expected = 0.016068779876656947
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-248.html','orange')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #299 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-248.html and word orange\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #299 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-248.html and word orange\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #300 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-248.html and word coconut
expected = 0.030383732717892357
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-248.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #300 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-248.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #300 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-248.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #301 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-248.html and word pear
expected = 0.016689904422743936
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-248.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #301 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-248.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #301 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-248.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #302 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-248.html and word blueberry
expected = 0.016378992417115296
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-248.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #302 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-248.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #302 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-248.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #303 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-248.html and word papaya
expected = 0.026442080475847483
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-248.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #303 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-248.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #303 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-248.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #304 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-248.html and word banana
expected = 0.026572952319559886
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-248.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #304 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-248.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #304 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-248.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #305 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-248.html and word apricot
expected = 0.015913934923746677
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-248.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #305 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-248.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #305 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-248.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #306 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-248.html and word peach
expected = 0.006240636909290333
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-248.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #306 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-248.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #306 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-248.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #307 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-248.html and word fig
expected = 0.012814374932723162
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-248.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #307 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-248.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #307 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-248.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #308 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-248.html and word lime
expected = 0.03138951791793268
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-248.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #308 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-248.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #308 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-248.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #309 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-248.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-248.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #309 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-248.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #309 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-248.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #310 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-96.html and word orange
expected = 0.00630035086051498
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-96.html','orange')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #310 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-96.html and word orange\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #310 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-96.html and word orange\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #311 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-96.html and word coconut
expected = 0.01985841508838385
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-96.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #311 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-96.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #311 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-96.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #312 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-96.html and word pear
expected = 0.012922084844447151
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-96.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #312 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-96.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #312 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-96.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #313 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-96.html and word blueberry
expected = 0.041801141325017145
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-96.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #313 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-96.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #313 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-96.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #314 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-96.html and word papaya
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-96.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #314 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-96.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #314 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-96.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #315 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-96.html and word banana
expected = 0.011723864950498685
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-96.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #315 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-96.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #315 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-96.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #316 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-96.html and word apricot
expected = 0.012321293884309515
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-96.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #316 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-96.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #316 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-96.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #317 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-96.html and word peach
expected = 0.028541165656991215
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-96.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #317 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-96.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #317 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-96.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #318 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-96.html and word fig
expected = 0.02969362560661244
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-96.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #318 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-96.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #318 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-96.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #319 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-96.html and word lime
expected = 0.007840756246468723
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-96.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #319 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-96.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #319 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-96.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #320 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-96.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-96.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #320 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-96.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #320 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-96.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #321 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-445.html and word orange
expected = 0.012441181905748045
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-445.html','orange')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #321 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-445.html and word orange\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #321 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-445.html and word orange\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #322 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-445.html and word coconut
expected = 0.023655238248076776
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-445.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #322 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-445.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #322 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-445.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #323 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-445.html and word pear
expected = 0.020368698578779244
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-445.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #323 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-445.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #323 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-445.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #324 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-445.html and word blueberry
expected = 0.01514140644807256
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-445.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #324 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-445.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #324 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-445.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #325 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-445.html and word papaya
expected = 0.02055874156450231
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-445.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #325 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-445.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #325 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-445.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #326 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-445.html and word banana
expected = 0.020688357283494996
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-445.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #326 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-445.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #326 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-445.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #327 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-445.html and word apricot
expected = 0.017078133808728583
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-445.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #327 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-445.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #327 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-445.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #328 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-445.html and word peach
expected = 0.014140510590035458
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-445.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #328 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-445.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #328 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-445.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #329 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-445.html and word fig
expected = 0.021742602047176804
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-445.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #329 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-445.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #329 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-445.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #330 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-445.html and word lime
expected = 0.015482990852508524
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-445.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #330 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-445.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #330 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-445.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #331 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-445.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-445.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #331 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-445.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #331 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-445.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #332 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-236.html and word orange
expected = 0.016450361951706637
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-236.html','orange')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #332 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-236.html and word orange\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #332 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-236.html and word orange\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #333 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-236.html and word coconut
expected = 0.049931024677322175
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-236.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #333 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-236.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #333 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-236.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #334 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-236.html and word pear
expected = 0.033086877768875915
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-236.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #334 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-236.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #334 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-236.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #335 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-236.html and word blueberry
expected = 0.008526098947947307
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-236.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #335 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-236.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #335 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-236.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #336 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-236.html and word papaya
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-236.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #336 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-236.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #336 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-236.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #337 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-236.html and word banana
expected = 0.01550188907852276
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-236.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #337 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-236.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #337 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-236.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #338 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-236.html and word apricot
expected = 0.004177715151110465
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-236.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #338 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-236.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #338 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-236.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #339 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-236.html and word peach
expected = 0.019413909687507308
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-236.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #339 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-236.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #339 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-236.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #340 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-236.html and word fig
expected = 0.01629183992692806
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-236.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #340 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-236.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #340 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-236.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #341 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-236.html and word lime
expected = 0.0253806691530656
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-236.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #341 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-236.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #341 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-236.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #342 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-236.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-236.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #342 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-236.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #342 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-236.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #343 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-298.html and word orange
expected = 0.026012389487530613
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-298.html','orange')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #343 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-298.html and word orange\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #343 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-298.html and word orange\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #344 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-298.html and word coconut
expected = 0.014389509232181368
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-298.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #344 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-298.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #344 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-298.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #345 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-298.html and word pear
expected = 0.01832993104636552
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-298.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #345 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-298.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #345 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-298.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #346 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-298.html and word blueberry
expected = 0.026514566347768845
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-298.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #346 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-298.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #346 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-298.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #347 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-298.html and word papaya
expected = 0.022923253473122573
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-298.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #347 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-298.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #347 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-298.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #348 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-298.html and word banana
expected = 0.012584752053965092
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-298.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #348 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-298.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #348 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-298.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #349 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-298.html and word apricot
expected = 0.008897778933320092
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-298.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #349 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-298.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #349 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-298.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #350 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-298.html and word peach
expected = 0.012712724945353939
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-298.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #350 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-298.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #350 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-298.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #351 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-298.html and word fig
expected = 0.004490085242472446
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-298.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #351 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-298.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #351 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-298.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #352 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-298.html and word lime
expected = 0.03744555789446262
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-298.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #352 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-298.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #352 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-298.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #353 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-298.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-298.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #353 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-298.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #353 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-298.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #354 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-937.html and word orange
expected = 0.023618090863966823
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-937.html','orange')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #354 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-937.html and word orange\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #354 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-937.html and word orange\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #355 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-937.html and word coconut
expected = 0.02812856345047595
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-937.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #355 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-937.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #355 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-937.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #356 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-937.html and word pear
expected = 0.01119852905304813
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-937.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #356 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-937.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #356 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-937.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #357 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-937.html and word blueberry
expected = 0.008287894509765208
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-937.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #357 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-937.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #357 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-937.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #358 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-937.html and word papaya
expected = 0.01946229882081863
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-937.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #358 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-937.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #358 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-937.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #359 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-937.html and word banana
expected = 0.019887777635724264
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-937.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #359 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-937.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #359 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-937.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #360 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-937.html and word apricot
expected = 0.008052571887478177
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-937.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #360 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-937.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #360 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-937.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #361 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-937.html and word peach
expected = 0.027194867326669574
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-937.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #361 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-937.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #361 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-937.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #362 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-937.html and word fig
expected = 0.02339049784223565
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-937.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #362 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-937.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #362 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-937.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #363 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-937.html and word lime
expected = 0.01668115800763583
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-937.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #363 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-937.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #363 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-937.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #364 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-937.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-937.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #364 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-937.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #364 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-937.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #365 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-286.html and word orange
expected = 0.012973673602372159
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-286.html','orange')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #365 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-286.html and word orange\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #365 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-286.html and word orange\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #366 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-286.html and word coconut
expected = 0.024647473389395737
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-286.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #366 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-286.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #366 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-286.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #367 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-286.html and word pear
expected = 0.016085809038092855
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-286.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #367 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-286.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #367 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-286.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #368 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-286.html and word blueberry
expected = 0.015786150572501084
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-286.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #368 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-286.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #368 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-286.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #369 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-286.html and word papaya
expected = 0.026511064720393444
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-286.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #369 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-286.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #369 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-286.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #370 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-286.html and word banana
expected = 0.0169385076092213
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-286.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #370 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-286.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #370 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-286.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #371 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-286.html and word apricot
expected = 0.022654610355386354
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-286.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #371 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-286.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #371 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-286.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #372 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-286.html and word peach
expected = 0.017110753338439387
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-286.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #372 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-286.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #372 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-286.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #373 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-286.html and word fig
expected = 0.012848654285818393
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-286.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #373 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-286.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #373 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-286.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #374 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-286.html and word lime
expected = 0.025434165323944054
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-286.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #374 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-286.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #374 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-286.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #375 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-286.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-286.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #375 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-286.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #375 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-286.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #376 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-719.html and word orange
expected = 0.022209610921890024
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-719.html','orange')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #376 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-719.html and word orange\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #376 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-719.html and word orange\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #377 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-719.html and word coconut
expected = 0.003555747332861075
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-719.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #377 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-719.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #377 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-719.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #378 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-719.html and word pear
expected = 0.02619765248366744
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-719.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #378 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-719.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #378 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-719.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #379 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-719.html and word blueberry
expected = 0.009957011422811586
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-719.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #379 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-719.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #379 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-719.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #380 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-719.html and word papaya
expected = 0.020084851260442894
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-719.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #380 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-719.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #380 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-719.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #381 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-719.html and word banana
expected = 0.020929079007442043
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-719.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #381 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-719.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #381 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-719.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #382 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-719.html and word apricot
expected = 0.015913934923746677
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-719.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #382 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-719.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #382 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-719.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #383 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-719.html and word peach
expected = 0.03783998647342168
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-719.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #383 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-719.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #383 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-719.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #384 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-719.html and word fig
expected = 0.024979635965552856
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-719.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #384 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-719.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #384 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-719.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #385 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-719.html and word lime
expected = 0.016102598617230034
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-719.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #385 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-719.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #385 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-719.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #386 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-719.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-719.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #386 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-719.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #386 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-719.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #387 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-524.html and word orange
expected = 0.009512978892062937
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-524.html','orange')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #387 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-524.html and word orange\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #387 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-524.html and word orange\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #388 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-524.html and word coconut
expected = 0.02490868620220216
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-524.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #388 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-524.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #388 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-524.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #389 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-524.html and word pear
expected = 0.009880694719999028
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-524.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #389 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-524.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #389 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-524.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #390 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-524.html and word blueberry
expected = 0.009696629758655519
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-524.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #390 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-524.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #390 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-524.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #391 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-524.html and word papaya
expected = 0.014816380444183387
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-524.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #391 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-524.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #391 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-524.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #392 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-524.html and word banana
expected = 0.03588560200206767
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-524.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #392 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-524.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #392 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-524.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #393 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-524.html and word apricot
expected = 0.02070096558111657
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-524.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #393 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-524.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #393 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-524.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #394 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-524.html and word peach
expected = 0.01989752601240955
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-524.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #394 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-524.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #394 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-524.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #395 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-524.html and word fig
expected = 0.02070096558111657
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-524.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #395 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-524.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #395 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-524.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #396 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-524.html and word lime
expected = 0.02876958206099301
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-524.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #396 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-524.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #396 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-524.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #397 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-524.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-524.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #397 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-524.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #397 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-524.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #398 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word orange
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','orange')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #398 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word orange\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #398 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word orange\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #399 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word coconut
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #399 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #399 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word coconut\n\n')
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


#Test #401 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word blueberry
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #401 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #401 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #402 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word papaya
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #402 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #402 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word papaya\n\n')
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


#Test #404 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word apricot
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #404 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #404 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #405 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word peach
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #405 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #405 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #406 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word fig
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #406 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #406 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #407 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word lime
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #407 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #407 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word lime\n\n')
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









output = open('fruits3-all-search-failed.txt', 'w')
success_output = open('fruits3-all-search-passed.txt', 'w')

#Test #409 checking search results for 'apricot apple orange blueberry cherry fig tomato' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-500.html', 'title': 'N-500', 'score': 0.996657140631476}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-150.html', 'title': 'N-150', 'score': 0.9964896314972754}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-893.html', 'title': 'N-893', 'score': 0.9955832957419136}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-392.html', 'title': 'N-392', 'score': 0.9952222631285036}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-704.html', 'title': 'N-704', 'score': 0.993598093337766}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-768.html', 'title': 'N-768', 'score': 0.9922305853094192}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-847.html', 'title': 'N-847', 'score': 0.9919565113255885}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-639.html', 'title': 'N-639', 'score': 0.9917263677341843}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-805.html', 'title': 'N-805', 'score': 0.9916828383867053}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-481.html', 'title': 'N-481', 'score': 0.9907790665981752}]
result = search.search('apricot apple orange blueberry cherry fig tomato',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #409 checking search results for 'apricot apple orange blueberry cherry fig tomato' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #409 checking search results for 'apricot apple orange blueberry cherry fig tomato' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #410 checking search results for 'peach kiwi fig coconut fig cherry' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-179.html', 'title': 'N-179', 'score': 0.9990249112721261}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-511.html', 'title': 'N-511', 'score': 0.997463008361324}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-708.html', 'title': 'N-708', 'score': 0.9969279011432896}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-565.html', 'title': 'N-565', 'score': 0.9960298222060158}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-821.html', 'title': 'N-821', 'score': 0.9959013770886663}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-267.html', 'title': 'N-267', 'score': 0.9947915253090048}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-903.html', 'title': 'N-903', 'score': 0.9929983051589008}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-122.html', 'title': 'N-122', 'score': 0.9928332868117464}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-631.html', 'title': 'N-631', 'score': 0.9925721548913505}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-593.html', 'title': 'N-593', 'score': 0.9923064638409166}]
result = search.search('peach kiwi fig coconut fig cherry',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #410 checking search results for 'peach kiwi fig coconut fig cherry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #410 checking search results for 'peach kiwi fig coconut fig cherry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #411 checking search results for 'lime banana fig peach cherry blueberry papaya' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-966.html', 'title': 'N-966', 'score': 0.9959862761718974}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-529.html', 'title': 'N-529', 'score': 0.9944456811861644}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-776.html', 'title': 'N-776', 'score': 0.993556389785798}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-854.html', 'title': 'N-854', 'score': 0.9933223859730214}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-707.html', 'title': 'N-707', 'score': 0.9932973817676394}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-560.html', 'title': 'N-560', 'score': 0.9920928140853758}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-843.html', 'title': 'N-843', 'score': 0.9903564476512949}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-639.html', 'title': 'N-639', 'score': 0.9899210594358798}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-48.html', 'title': 'N-48', 'score': 0.9891959598427487}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-879.html', 'title': 'N-879', 'score': 0.9887895558135363}]
result = search.search('lime banana fig peach cherry blueberry papaya',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #411 checking search results for 'lime banana fig peach cherry blueberry papaya' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #411 checking search results for 'lime banana fig peach cherry blueberry papaya' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #412 checking search results for 'cherry coconut apricot apple pear pear' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-846.html', 'title': 'N-846', 'score': 0.9998765175320621}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-178.html', 'title': 'N-178', 'score': 0.9922995844011827}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-367.html', 'title': 'N-367', 'score': 0.9921885385157808}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-797.html', 'title': 'N-797', 'score': 0.9917813919035491}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-102.html', 'title': 'N-102', 'score': 0.9912398198654265}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-70.html', 'title': 'N-70', 'score': 0.9899795800993891}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-258.html', 'title': 'N-258', 'score': 0.9898586724683701}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-572.html', 'title': 'N-572', 'score': 0.9897076972769996}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-254.html', 'title': 'N-254', 'score': 0.9896129160844085}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-867.html', 'title': 'N-867', 'score': 0.9886954755183917}]
result = search.search('cherry coconut apricot apple pear pear',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #412 checking search results for 'cherry coconut apricot apple pear pear' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #412 checking search results for 'cherry coconut apricot apple pear pear' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #413 checking search results for 'papaya lime blueberry banana orange' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-188.html', 'title': 'N-188', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-375.html', 'title': 'N-375', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-48.html', 'title': 'N-48', 'score': 0.997920298201408}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-966.html', 'title': 'N-966', 'score': 0.9972929932405408}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-453.html', 'title': 'N-453', 'score': 0.9968138985782268}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-594.html', 'title': 'N-594', 'score': 0.9961974990752348}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-706.html', 'title': 'N-706', 'score': 0.9961618394033934}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-879.html', 'title': 'N-879', 'score': 0.9960305035049896}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-957.html', 'title': 'N-957', 'score': 0.9939021491810179}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-921.html', 'title': 'N-921', 'score': 0.9937768578652273}]
result = search.search('papaya lime blueberry banana orange',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #413 checking search results for 'papaya lime blueberry banana orange' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #413 checking search results for 'papaya lime blueberry banana orange' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #414 checking search results for 'peach papaya peach coconut lime apple papaya' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-906.html', 'title': 'N-906', 'score': 0.9942066636960032}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-753.html', 'title': 'N-753', 'score': 0.9937375528176168}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-419.html', 'title': 'N-419', 'score': 0.9931739455489959}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-888.html', 'title': 'N-888', 'score': 0.9929930672997033}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-409.html', 'title': 'N-409', 'score': 0.9928730186812321}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-277.html', 'title': 'N-277', 'score': 0.9927912115013574}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-588.html', 'title': 'N-588', 'score': 0.9922382164886667}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-84.html', 'title': 'N-84', 'score': 0.9918547651847941}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-872.html', 'title': 'N-872', 'score': 0.991515397044009}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-221.html', 'title': 'N-221', 'score': 0.9913058119893996}]
result = search.search('peach papaya peach coconut lime apple papaya',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #414 checking search results for 'peach papaya peach coconut lime apple papaya' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #414 checking search results for 'peach papaya peach coconut lime apple papaya' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #415 checking search results for 'banana banana orange cherry coconut pear apple' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-301.html', 'title': 'N-301', 'score': 0.9949706578581397}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-958.html', 'title': 'N-958', 'score': 0.993710277384931}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-704.html', 'title': 'N-704', 'score': 0.9924942361094691}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-104.html', 'title': 'N-104', 'score': 0.9917553337100913}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-699.html', 'title': 'N-699', 'score': 0.9887429643703739}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-725.html', 'title': 'N-725', 'score': 0.9884690094360766}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-989.html', 'title': 'N-989', 'score': 0.9882864178982671}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-872.html', 'title': 'N-872', 'score': 0.9876849503279309}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-49.html', 'title': 'N-49', 'score': 0.9872551396673125}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-148.html', 'title': 'N-148', 'score': 0.9845244470297918}]
result = search.search('banana banana orange cherry coconut pear apple',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #415 checking search results for 'banana banana orange cherry coconut pear apple' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #415 checking search results for 'banana banana orange cherry coconut pear apple' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #416 checking search results for 'banana pear apricot fig orange banana peach banana' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-113.html', 'title': 'N-113', 'score': 0.9934100443134014}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-49.html', 'title': 'N-49', 'score': 0.9892200325884043}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-535.html', 'title': 'N-535', 'score': 0.9862836218555191}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-689.html', 'title': 'N-689', 'score': 0.9814667381696385}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-872.html', 'title': 'N-872', 'score': 0.9794783762346252}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-812.html', 'title': 'N-812', 'score': 0.9788356471491955}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-450.html', 'title': 'N-450', 'score': 0.9771113967245222}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-477.html', 'title': 'N-477', 'score': 0.9765760467570218}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-238.html', 'title': 'N-238', 'score': 0.9764115061650036}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-42.html', 'title': 'N-42', 'score': 0.9762241526833717}]
result = search.search('banana pear apricot fig orange banana peach banana',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #416 checking search results for 'banana pear apricot fig orange banana peach banana' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #416 checking search results for 'banana pear apricot fig orange banana peach banana' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #417 checking search results for 'coconut banana peach kiwi peach banana apricot cherry' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-434.html', 'title': 'N-434', 'score': 0.9999792202398612}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-354.html', 'title': 'N-354', 'score': 0.9931025942755201}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-704.html', 'title': 'N-704', 'score': 0.9918520410869637}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-979.html', 'title': 'N-979', 'score': 0.9894853588035857}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-396.html', 'title': 'N-396', 'score': 0.9891762623398717}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-155.html', 'title': 'N-155', 'score': 0.9887428520182793}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-120.html', 'title': 'N-120', 'score': 0.9886444070750399}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-296.html', 'title': 'N-296', 'score': 0.9875371314077857}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-102.html', 'title': 'N-102', 'score': 0.9864348207155651}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-588.html', 'title': 'N-588', 'score': 0.9856403777533278}]
result = search.search('coconut banana peach kiwi peach banana apricot cherry',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #417 checking search results for 'coconut banana peach kiwi peach banana apricot cherry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #417 checking search results for 'coconut banana peach kiwi peach banana apricot cherry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #418 checking search results for 'pear coconut cherry fig banana blueberry apple' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-768.html', 'title': 'N-768', 'score': 0.9984174376189461}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-500.html', 'title': 'N-500', 'score': 0.9971945279126039}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-392.html', 'title': 'N-392', 'score': 0.9962212550696288}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-394.html', 'title': 'N-394', 'score': 0.9945902740493247}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-734.html', 'title': 'N-734', 'score': 0.9943097147744091}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-843.html', 'title': 'N-843', 'score': 0.9924518195485746}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-560.html', 'title': 'N-560', 'score': 0.9910157537212039}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-481.html', 'title': 'N-481', 'score': 0.9897463066576035}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-776.html', 'title': 'N-776', 'score': 0.9890483163366132}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-567.html', 'title': 'N-567', 'score': 0.9868078344810973}]
result = search.search('pear coconut cherry fig banana blueberry apple',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #418 checking search results for 'pear coconut cherry fig banana blueberry apple' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #418 checking search results for 'pear coconut cherry fig banana blueberry apple' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #419 checking search results for 'pear orange lime pear kiwi' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-476.html', 'title': 'N-476', 'score': 0.9997735938080132}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-242.html', 'title': 'N-242', 'score': 0.9997445416604961}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-250.html', 'title': 'N-250', 'score': 0.999705408247804}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-638.html', 'title': 'N-638', 'score': 0.9995552687273664}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-96.html', 'title': 'N-96', 'score': 0.9994305624612911}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-187.html', 'title': 'N-187', 'score': 0.9983114069232555}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-763.html', 'title': 'N-763', 'score': 0.997232988250687}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-162.html', 'title': 'N-162', 'score': 0.9968199762974823}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-743.html', 'title': 'N-743', 'score': 0.9963801110426173}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-501.html', 'title': 'N-501', 'score': 0.9959964947756115}]
result = search.search('pear orange lime pear kiwi',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #419 checking search results for 'pear orange lime pear kiwi' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #419 checking search results for 'pear orange lime pear kiwi' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #420 checking search results for 'fig banana peach fig fig' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-160.html', 'title': 'N-160', 'score': 0.9999991550058964}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-867.html', 'title': 'N-867', 'score': 0.9999632066442723}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-136.html', 'title': 'N-136', 'score': 0.999670352884885}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-16.html', 'title': 'N-16', 'score': 0.9992903738827942}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-598.html', 'title': 'N-598', 'score': 0.9992327569855431}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-38.html', 'title': 'N-38', 'score': 0.9990222378018603}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-819.html', 'title': 'N-819', 'score': 0.9989951420246397}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-669.html', 'title': 'N-669', 'score': 0.9988463445197154}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-405.html', 'title': 'N-405', 'score': 0.9977874804388472}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-936.html', 'title': 'N-936', 'score': 0.9971553368019597}]
result = search.search('fig banana peach fig fig',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #420 checking search results for 'fig banana peach fig fig' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #420 checking search results for 'fig banana peach fig fig' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #421 checking search results for 'lime apple apricot papaya apple fig apricot fig' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-392.html', 'title': 'N-392', 'score': 0.9952895264417714}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-137.html', 'title': 'N-137', 'score': 0.995278500105583}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-187.html', 'title': 'N-187', 'score': 0.9923611905816038}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-775.html', 'title': 'N-775', 'score': 0.9921349818177484}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-497.html', 'title': 'N-497', 'score': 0.9914034425066942}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-81.html', 'title': 'N-81', 'score': 0.9912932010106521}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-67.html', 'title': 'N-67', 'score': 0.990145908539482}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-806.html', 'title': 'N-806', 'score': 0.9883576779150736}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-968.html', 'title': 'N-968', 'score': 0.9880716890845698}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-311.html', 'title': 'N-311', 'score': 0.9872879661613129}]
result = search.search('lime apple apricot papaya apple fig apricot fig',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #421 checking search results for 'lime apple apricot papaya apple fig apricot fig' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #421 checking search results for 'lime apple apricot papaya apple fig apricot fig' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #422 checking search results for 'cherry fig orange tomato blueberry apricot kiwi cherry' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-49.html', 'title': 'N-49', 'score': 0.9933394451481747}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-399.html', 'title': 'N-399', 'score': 0.9929767337770048}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-408.html', 'title': 'N-408', 'score': 0.9901807117841042}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-972.html', 'title': 'N-972', 'score': 0.9900736605084641}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-535.html', 'title': 'N-535', 'score': 0.9899043417781186}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-644.html', 'title': 'N-644', 'score': 0.989584423104155}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-974.html', 'title': 'N-974', 'score': 0.9874146392309686}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-760.html', 'title': 'N-760', 'score': 0.9859916519793874}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-852.html', 'title': 'N-852', 'score': 0.9848597686071561}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-659.html', 'title': 'N-659', 'score': 0.9833541705351202}]
result = search.search('cherry fig orange tomato blueberry apricot kiwi cherry',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #422 checking search results for 'cherry fig orange tomato blueberry apricot kiwi cherry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #422 checking search results for 'cherry fig orange tomato blueberry apricot kiwi cherry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #423 checking search results for 'pear lime pear banana apricot blueberry apple' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-749.html', 'title': 'N-749', 'score': 0.9999200628352071}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-323.html', 'title': 'N-323', 'score': 0.9977736520885074}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-270.html', 'title': 'N-270', 'score': 0.9927594668865691}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-293.html', 'title': 'N-293', 'score': 0.9923406538981087}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-482.html', 'title': 'N-482', 'score': 0.9922132635807248}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-178.html', 'title': 'N-178', 'score': 0.9909340930238996}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-439.html', 'title': 'N-439', 'score': 0.9904676565501297}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-594.html', 'title': 'N-594', 'score': 0.9902721096470317}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-933.html', 'title': 'N-933', 'score': 0.9883859956695845}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-902.html', 'title': 'N-902', 'score': 0.9878263275539723}]
result = search.search('pear lime pear banana apricot blueberry apple',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #423 checking search results for 'pear lime pear banana apricot blueberry apple' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #423 checking search results for 'pear lime pear banana apricot blueberry apple' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #424 checking search results for 'papaya blueberry papaya banana banana kiwi lime' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-868.html', 'title': 'N-868', 'score': 0.9999419208423923}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-155.html', 'title': 'N-155', 'score': 0.9975907970336472}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-396.html', 'title': 'N-396', 'score': 0.9962774999155775}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-97.html', 'title': 'N-97', 'score': 0.9948843644595005}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-120.html', 'title': 'N-120', 'score': 0.9947281950317498}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-638.html', 'title': 'N-638', 'score': 0.9933093894780947}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-628.html', 'title': 'N-628', 'score': 0.9908730412736365}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-240.html', 'title': 'N-240', 'score': 0.9902125156457922}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-230.html', 'title': 'N-230', 'score': 0.9901040184419275}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-743.html', 'title': 'N-743', 'score': 0.9890234974961156}]
result = search.search('papaya blueberry papaya banana banana kiwi lime',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #424 checking search results for 'papaya blueberry papaya banana banana kiwi lime' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #424 checking search results for 'papaya blueberry papaya banana banana kiwi lime' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #425 checking search results for 'papaya pear banana blueberry cherry cherry lime kiwi' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-451.html', 'title': 'N-451', 'score': 0.9942767348670141}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-694.html', 'title': 'N-694', 'score': 0.9921004540778505}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-334.html', 'title': 'N-334', 'score': 0.9878219220184973}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-823.html', 'title': 'N-823', 'score': 0.9857033076940905}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-318.html', 'title': 'N-318', 'score': 0.9848357482192017}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-293.html', 'title': 'N-293', 'score': 0.9847780747680684}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-180.html', 'title': 'N-180', 'score': 0.9833637995663949}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-55.html', 'title': 'N-55', 'score': 0.9831658401403833}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-117.html', 'title': 'N-117', 'score': 0.9830625229582559}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-757.html', 'title': 'N-757', 'score': 0.980843092251259}]
result = search.search('papaya pear banana blueberry cherry cherry lime kiwi',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #425 checking search results for 'papaya pear banana blueberry cherry cherry lime kiwi' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #425 checking search results for 'papaya pear banana blueberry cherry cherry lime kiwi' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #426 checking search results for 'cherry apricot lime cherry apple coconut apricot apple' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-347.html', 'title': 'N-347', 'score': 0.9957579447472868}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-328.html', 'title': 'N-328', 'score': 0.995726208393656}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-371.html', 'title': 'N-371', 'score': 0.9928075448858114}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-574.html', 'title': 'N-574', 'score': 0.9919033312018768}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-277.html', 'title': 'N-277', 'score': 0.9913475046786338}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-852.html', 'title': 'N-852', 'score': 0.9904947476952705}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-654.html', 'title': 'N-654', 'score': 0.9895870263070089}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-913.html', 'title': 'N-913', 'score': 0.9892844766787824}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-554.html', 'title': 'N-554', 'score': 0.9883211924743374}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-230.html', 'title': 'N-230', 'score': 0.9882554715902596}]
result = search.search('cherry apricot lime cherry apple coconut apricot apple',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #426 checking search results for 'cherry apricot lime cherry apple coconut apricot apple' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #426 checking search results for 'cherry apricot lime cherry apple coconut apricot apple' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #427 checking search results for 'peach kiwi papaya peach coconut peach orange kiwi' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-6.html', 'title': 'N-6', 'score': 0.01419010758350642}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'title': 'N-0', 'score': 0.011884458946047791}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-5.html', 'title': 'N-5', 'score': 0.010135519106555538}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-25.html', 'title': 'N-25', 'score': 0.009988337508017621}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-4.html', 'title': 'N-4', 'score': 0.008240963525169374}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-10.html', 'title': 'N-10', 'score': 0.007367432407785363}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-2.html', 'title': 'N-2', 'score': 0.00635891404899202}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-3.html', 'title': 'N-3', 'score': 0.005893472050810722}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-241.html', 'title': 'N-241', 'score': 0.005870409703207553}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-7.html', 'title': 'N-7', 'score': 0.00585408337564403}]
result = search.search('peach kiwi papaya peach coconut peach orange kiwi',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #427 checking search results for 'peach kiwi papaya peach coconut peach orange kiwi' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #427 checking search results for 'peach kiwi papaya peach coconut peach orange kiwi' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #428 checking search results for 'peach kiwi papaya peach coconut peach orange kiwi' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-806.html', 'title': 'N-806', 'score': 0.9940147725243194}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-623.html', 'title': 'N-623', 'score': 0.9907640710487274}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-602.html', 'title': 'N-602', 'score': 0.9902175624379462}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-170.html', 'title': 'N-170', 'score': 0.9893938196807692}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-37.html', 'title': 'N-37', 'score': 0.9885185817113674}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-959.html', 'title': 'N-959', 'score': 0.988450365229997}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-432.html', 'title': 'N-432', 'score': 0.9859947901574087}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-803.html', 'title': 'N-803', 'score': 0.9850912657645244}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-426.html', 'title': 'N-426', 'score': 0.9844803752994762}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-197.html', 'title': 'N-197', 'score': 0.9829308690285856}]
result = search.search('peach kiwi papaya peach coconut peach orange kiwi',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #428 checking search results for 'peach kiwi papaya peach coconut peach orange kiwi' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #428 checking search results for 'peach kiwi papaya peach coconut peach orange kiwi' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #429 checking search results for 'orange lime peach kiwi apricot peach banana' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-99.html', 'title': 'N-99', 'score': 0.9920523810173528}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-481.html', 'title': 'N-481', 'score': 0.9913845949946545}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-906.html', 'title': 'N-906', 'score': 0.990479756262042}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-409.html', 'title': 'N-409', 'score': 0.9900028099690634}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-959.html', 'title': 'N-959', 'score': 0.9894744763943999}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-755.html', 'title': 'N-755', 'score': 0.9890337187420464}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-735.html', 'title': 'N-735', 'score': 0.9882474259406471}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-460.html', 'title': 'N-460', 'score': 0.987870727336512}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-386.html', 'title': 'N-386', 'score': 0.9875796685526746}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-28.html', 'title': 'N-28', 'score': 0.9869906825509336}]
result = search.search('orange lime peach kiwi apricot peach banana',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #429 checking search results for 'orange lime peach kiwi apricot peach banana' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #429 checking search results for 'orange lime peach kiwi apricot peach banana' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #430 checking search results for 'coconut peach apple banana apricot kiwi pear cherry' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-500.html', 'title': 'N-500', 'score': 0.9976356827723393}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-18.html', 'title': 'N-18', 'score': 0.9924689147585533}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-560.html', 'title': 'N-560', 'score': 0.9915850326233516}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-483.html', 'title': 'N-483', 'score': 0.9907744309840341}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-128.html', 'title': 'N-128', 'score': 0.9894622503606325}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-886.html', 'title': 'N-886', 'score': 0.9884759446167776}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-567.html', 'title': 'N-567', 'score': 0.9883807406191444}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-843.html', 'title': 'N-843', 'score': 0.9867766878436215}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-734.html', 'title': 'N-734', 'score': 0.9854401734839516}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-536.html', 'title': 'N-536', 'score': 0.9853778015273618}]
result = search.search('coconut peach apple banana apricot kiwi pear cherry',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #430 checking search results for 'coconut peach apple banana apricot kiwi pear cherry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #430 checking search results for 'coconut peach apple banana apricot kiwi pear cherry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #431 checking search results for 'orange orange lime orange banana blueberry fig peach' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-117.html', 'title': 'N-117', 'score': 0.9940153703471427}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-850.html', 'title': 'N-850', 'score': 0.9905731150469387}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-558.html', 'title': 'N-558', 'score': 0.9868285114368797}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-990.html', 'title': 'N-990', 'score': 0.9808744396772848}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-575.html', 'title': 'N-575', 'score': 0.977353550296544}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-262.html', 'title': 'N-262', 'score': 0.9761575862445466}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-412.html', 'title': 'N-412', 'score': 0.9761477265825135}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-679.html', 'title': 'N-679', 'score': 0.9724593545524212}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-636.html', 'title': 'N-636', 'score': 0.9703244622779825}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-371.html', 'title': 'N-371', 'score': 0.9695578029221673}]
result = search.search('orange orange lime orange banana blueberry fig peach',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #431 checking search results for 'orange orange lime orange banana blueberry fig peach' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #431 checking search results for 'orange orange lime orange banana blueberry fig peach' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #432 checking search results for 'kiwi papaya apricot pear pear tomato banana cherry' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-867.html', 'title': 'N-867', 'score': 0.9961398405160612}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-825.html', 'title': 'N-825', 'score': 0.9924626332564589}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-555.html', 'title': 'N-555', 'score': 0.991593440187997}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-938.html', 'title': 'N-938', 'score': 0.989321703679223}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-162.html', 'title': 'N-162', 'score': 0.986520951415104}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-698.html', 'title': 'N-698', 'score': 0.9863688809257959}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-126.html', 'title': 'N-126', 'score': 0.986263584954034}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-135.html', 'title': 'N-135', 'score': 0.985891344474402}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-323.html', 'title': 'N-323', 'score': 0.9856739305437286}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-930.html', 'title': 'N-930', 'score': 0.9855039483841519}]
result = search.search('kiwi papaya apricot pear pear tomato banana cherry',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #432 checking search results for 'kiwi papaya apricot pear pear tomato banana cherry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #432 checking search results for 'kiwi papaya apricot pear pear tomato banana cherry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #433 checking search results for 'lime apricot papaya cherry lime pear tomato' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-500.html', 'title': 'N-500', 'score': 0.9992487158939609}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-208.html', 'title': 'N-208', 'score': 0.9982575746074941}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-101.html', 'title': 'N-101', 'score': 0.9946121578157056}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-165.html', 'title': 'N-165', 'score': 0.9944362436282751}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-915.html', 'title': 'N-915', 'score': 0.9941012813401298}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-936.html', 'title': 'N-936', 'score': 0.9937508649098679}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-673.html', 'title': 'N-673', 'score': 0.9934471556098442}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-309.html', 'title': 'N-309', 'score': 0.9921768588707706}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-894.html', 'title': 'N-894', 'score': 0.9921482828528138}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-437.html', 'title': 'N-437', 'score': 0.9919355506949827}]
result = search.search('lime apricot papaya cherry lime pear tomato',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #433 checking search results for 'lime apricot papaya cherry lime pear tomato' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #433 checking search results for 'lime apricot papaya cherry lime pear tomato' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #434 checking search results for 'tomato blueberry papaya cherry blueberry coconut papaya peach' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-778.html', 'title': 'N-778', 'score': 0.9999606590164716}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-82.html', 'title': 'N-82', 'score': 0.9987456474782834}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-158.html', 'title': 'N-158', 'score': 0.9940870578953088}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-957.html', 'title': 'N-957', 'score': 0.9931737228269907}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-866.html', 'title': 'N-866', 'score': 0.9919983057374997}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-483.html', 'title': 'N-483', 'score': 0.9897266992241088}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-753.html', 'title': 'N-753', 'score': 0.9894579825473147}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-565.html', 'title': 'N-565', 'score': 0.9884994891840077}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-548.html', 'title': 'N-548', 'score': 0.9884795150579894}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-250.html', 'title': 'N-250', 'score': 0.9882121140039851}]
result = search.search('tomato blueberry papaya cherry blueberry coconut papaya peach',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #434 checking search results for 'tomato blueberry papaya cherry blueberry coconut papaya peach' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #434 checking search results for 'tomato blueberry papaya cherry blueberry coconut papaya peach' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #435 checking search results for 'peach tomato blueberry coconut kiwi tomato orange orange' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-540.html', 'title': 'N-540', 'score': 0.9949998926582546}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-92.html', 'title': 'N-92', 'score': 0.9923999380238355}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-800.html', 'title': 'N-800', 'score': 0.9923550110940008}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-708.html', 'title': 'N-708', 'score': 0.9907491424308845}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-690.html', 'title': 'N-690', 'score': 0.9906815074037743}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-513.html', 'title': 'N-513', 'score': 0.9902869507524845}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-417.html', 'title': 'N-417', 'score': 0.9901873445320463}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-291.html', 'title': 'N-291', 'score': 0.990142844832336}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-511.html', 'title': 'N-511', 'score': 0.9891073139085186}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-992.html', 'title': 'N-992', 'score': 0.9881138312408295}]
result = search.search('peach tomato blueberry coconut kiwi tomato orange orange',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #435 checking search results for 'peach tomato blueberry coconut kiwi tomato orange orange' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #435 checking search results for 'peach tomato blueberry coconut kiwi tomato orange orange' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #436 checking search results for 'orange tomato orange kiwi papaya blueberry cherry' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-273.html', 'title': 'N-273', 'score': 0.9963328411852623}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-323.html', 'title': 'N-323', 'score': 0.9948459869166972}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-558.html', 'title': 'N-558', 'score': 0.9944309207246316}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-574.html', 'title': 'N-574', 'score': 0.9935248073450057}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-894.html', 'title': 'N-894', 'score': 0.9929032094209235}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-888.html', 'title': 'N-888', 'score': 0.992889865338145}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-967.html', 'title': 'N-967', 'score': 0.992703396855212}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-386.html', 'title': 'N-386', 'score': 0.9922250321426875}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-277.html', 'title': 'N-277', 'score': 0.9913854511290167}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-708.html', 'title': 'N-708', 'score': 0.9907060090291135}]
result = search.search('orange tomato orange kiwi papaya blueberry cherry',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #436 checking search results for 'orange tomato orange kiwi papaya blueberry cherry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #436 checking search results for 'orange tomato orange kiwi papaya blueberry cherry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #437 checking search results for 'fig apricot peach kiwi banana kiwi fig kiwi' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-710.html', 'title': 'N-710', 'score': 0.999226311342578}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-508.html', 'title': 'N-508', 'score': 0.9903753970750445}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-879.html', 'title': 'N-879', 'score': 0.9901125461220764}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-970.html', 'title': 'N-970', 'score': 0.9882261603409201}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-275.html', 'title': 'N-275', 'score': 0.9876178864952675}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-4.html', 'title': 'N-4', 'score': 0.9856239683483008}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-220.html', 'title': 'N-220', 'score': 0.9855205786601788}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-561.html', 'title': 'N-561', 'score': 0.9851468340133184}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-367.html', 'title': 'N-367', 'score': 0.9835491323791408}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-778.html', 'title': 'N-778', 'score': 0.9833335131795822}]
result = search.search('fig apricot peach kiwi banana kiwi fig kiwi',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #437 checking search results for 'fig apricot peach kiwi banana kiwi fig kiwi' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #437 checking search results for 'fig apricot peach kiwi banana kiwi fig kiwi' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #438 checking search results for 'blueberry lime papaya coconut pear lime' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-64.html', 'title': 'N-64', 'score': 0.9999009184463747}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-500.html', 'title': 'N-500', 'score': 0.9989466032065155}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-704.html', 'title': 'N-704', 'score': 0.9952711128983477}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-659.html', 'title': 'N-659', 'score': 0.9952694015457665}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-101.html', 'title': 'N-101', 'score': 0.9944686797252221}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-611.html', 'title': 'N-611', 'score': 0.9938387826209336}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-360.html', 'title': 'N-360', 'score': 0.9929800026794308}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-806.html', 'title': 'N-806', 'score': 0.9924541855926899}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-708.html', 'title': 'N-708', 'score': 0.9916951612300934}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-488.html', 'title': 'N-488', 'score': 0.9911429606648161}]
result = search.search('blueberry lime papaya coconut pear lime',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #438 checking search results for 'blueberry lime papaya coconut pear lime' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #438 checking search results for 'blueberry lime papaya coconut pear lime' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #439 checking search results for 'peach apricot apricot coconut banana papaya coconut' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-923.html', 'title': 'N-923', 'score': 0.994313794190052}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-728.html', 'title': 'N-728', 'score': 0.9935599369400896}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-169.html', 'title': 'N-169', 'score': 0.9930890215183824}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-549.html', 'title': 'N-549', 'score': 0.9928357491994376}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-100.html', 'title': 'N-100', 'score': 0.991945863807794}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-679.html', 'title': 'N-679', 'score': 0.9917032890740224}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-185.html', 'title': 'N-185', 'score': 0.9903922636721124}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-968.html', 'title': 'N-968', 'score': 0.9903140496463608}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-160.html', 'title': 'N-160', 'score': 0.9902809305515372}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-919.html', 'title': 'N-919', 'score': 0.9902467243169184}]
result = search.search('peach apricot apricot coconut banana papaya coconut',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #439 checking search results for 'peach apricot apricot coconut banana papaya coconut' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #439 checking search results for 'peach apricot apricot coconut banana papaya coconut' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #440 checking search results for 'peach banana kiwi apple blueberry fig' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-500.html', 'title': 'N-500', 'score': 0.995496477674768}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-560.html', 'title': 'N-560', 'score': 0.9943797286360332}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-351.html', 'title': 'N-351', 'score': 0.9943479724558234}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-77.html', 'title': 'N-77', 'score': 0.9934474901965976}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-567.html', 'title': 'N-567', 'score': 0.9913281149815671}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-933.html', 'title': 'N-933', 'score': 0.9912212947590501}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-334.html', 'title': 'N-334', 'score': 0.9911006598163515}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-482.html', 'title': 'N-482', 'score': 0.991092480719417}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-707.html', 'title': 'N-707', 'score': 0.9904054482517853}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-694.html', 'title': 'N-694', 'score': 0.9900401976798281}]
result = search.search('peach banana kiwi apple blueberry fig',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #440 checking search results for 'peach banana kiwi apple blueberry fig' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #440 checking search results for 'peach banana kiwi apple blueberry fig' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #441 checking search results for 'pear apple tomato coconut apple blueberry pear' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-507.html', 'title': 'N-507', 'score': 0.9980245395744037}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-979.html', 'title': 'N-979', 'score': 0.9975431151378589}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-554.html', 'title': 'N-554', 'score': 0.9972754927540415}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-198.html', 'title': 'N-198', 'score': 0.9971004828554351}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-702.html', 'title': 'N-702', 'score': 0.9969836037172015}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-743.html', 'title': 'N-743', 'score': 0.9961211454100523}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-890.html', 'title': 'N-890', 'score': 0.995819563027123}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-668.html', 'title': 'N-668', 'score': 0.9955962070665104}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-215.html', 'title': 'N-215', 'score': 0.9955349490582889}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-126.html', 'title': 'N-126', 'score': 0.9951438047730663}]
result = search.search('pear apple tomato coconut apple blueberry pear',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #441 checking search results for 'pear apple tomato coconut apple blueberry pear' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #441 checking search results for 'pear apple tomato coconut apple blueberry pear' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #442 checking search results for 'kiwi fig peach apricot papaya apple kiwi' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-127.html', 'title': 'N-127', 'score': 0.9919713418601687}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-297.html', 'title': 'N-297', 'score': 0.9904994510240144}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-389.html', 'title': 'N-389', 'score': 0.9889922306385823}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-879.html', 'title': 'N-879', 'score': 0.9888373915446589}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-699.html', 'title': 'N-699', 'score': 0.9856720184255738}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-884.html', 'title': 'N-884', 'score': 0.9850880733330653}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-952.html', 'title': 'N-952', 'score': 0.9835967153399678}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-415.html', 'title': 'N-415', 'score': 0.9835040039227323}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-489.html', 'title': 'N-489', 'score': 0.983130480569476}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-456.html', 'title': 'N-456', 'score': 0.9820573430885322}]
result = search.search('kiwi fig peach apricot papaya apple kiwi',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #442 checking search results for 'kiwi fig peach apricot papaya apple kiwi' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #442 checking search results for 'kiwi fig peach apricot papaya apple kiwi' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #443 checking search results for 'kiwi lime blueberry papaya fig' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-449.html', 'title': 'N-449', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-557.html', 'title': 'N-557', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-958.html', 'title': 'N-958', 'score': 0.9975910526649828}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-453.html', 'title': 'N-453', 'score': 0.9968030464926082}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-560.html', 'title': 'N-560', 'score': 0.9966974904202078}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-571.html', 'title': 'N-571', 'score': 0.9965930555494517}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-408.html', 'title': 'N-408', 'score': 0.9962581259825845}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-538.html', 'title': 'N-538', 'score': 0.9957390943925863}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-698.html', 'title': 'N-698', 'score': 0.9957076728385323}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-912.html', 'title': 'N-912', 'score': 0.9952982253084878}]
result = search.search('kiwi lime blueberry papaya fig',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #443 checking search results for 'kiwi lime blueberry papaya fig' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #443 checking search results for 'kiwi lime blueberry papaya fig' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #444 checking search results for 'coconut cherry pear pear pear' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-938.html', 'title': 'N-938', 'score': 0.9996620091892984}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-511.html', 'title': 'N-511', 'score': 0.9996349753187103}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-623.html', 'title': 'N-623', 'score': 0.9992748113850048}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-822.html', 'title': 'N-822', 'score': 0.9991893067822185}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-874.html', 'title': 'N-874', 'score': 0.9991281009884566}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-932.html', 'title': 'N-932', 'score': 0.9988320286616779}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-162.html', 'title': 'N-162', 'score': 0.9981113605211874}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-912.html', 'title': 'N-912', 'score': 0.9975713058149209}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-957.html', 'title': 'N-957', 'score': 0.9975399876502873}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-548.html', 'title': 'N-548', 'score': 0.9972336362435874}]
result = search.search('coconut cherry pear pear pear',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #444 checking search results for 'coconut cherry pear pear pear' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #444 checking search results for 'coconut cherry pear pear pear' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #445 checking search results for 'tomato fig banana pear pear papaya blueberry' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-188.html', 'title': 'N-188', 'score': 0.9999022609553442}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-100.html', 'title': 'N-100', 'score': 0.994703065378252}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-705.html', 'title': 'N-705', 'score': 0.9931015476698072}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-622.html', 'title': 'N-622', 'score': 0.9907163844993693}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-77.html', 'title': 'N-77', 'score': 0.9906991552846434}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-237.html', 'title': 'N-237', 'score': 0.9906304088730052}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-743.html', 'title': 'N-743', 'score': 0.9898182173278883}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-371.html', 'title': 'N-371', 'score': 0.9893913993867003}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-482.html', 'title': 'N-482', 'score': 0.9888141345767292}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-117.html', 'title': 'N-117', 'score': 0.9885720010154277}]
result = search.search('tomato fig banana pear pear papaya blueberry',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #445 checking search results for 'tomato fig banana pear pear papaya blueberry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #445 checking search results for 'tomato fig banana pear pear papaya blueberry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #446 checking search results for 'fig apple coconut banana coconut apricot coconut' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-739.html', 'title': 'N-739', 'score': 0.9970026437644484}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-847.html', 'title': 'N-847', 'score': 0.9919778472586901}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-107.html', 'title': 'N-107', 'score': 0.9879473164342616}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-116.html', 'title': 'N-116', 'score': 0.9850182812917874}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-293.html', 'title': 'N-293', 'score': 0.984016885078703}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-887.html', 'title': 'N-887', 'score': 0.9834013294190365}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-899.html', 'title': 'N-899', 'score': 0.9816275920865851}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-636.html', 'title': 'N-636', 'score': 0.9805475917804934}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-578.html', 'title': 'N-578', 'score': 0.9801127374258783}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-90.html', 'title': 'N-90', 'score': 0.9800493199507939}]
result = search.search('fig apple coconut banana coconut apricot coconut',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #446 checking search results for 'fig apple coconut banana coconut apricot coconut' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #446 checking search results for 'fig apple coconut banana coconut apricot coconut' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #447 checking search results for 'coconut blueberry banana papaya cherry cherry apricot' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-594.html', 'title': 'N-594', 'score': 0.9966420945703943}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-690.html', 'title': 'N-690', 'score': 0.9953310513550436}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-659.html', 'title': 'N-659', 'score': 0.9928317320862973}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-78.html', 'title': 'N-78', 'score': 0.9927894998657772}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-463.html', 'title': 'N-463', 'score': 0.9886254791747818}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-334.html', 'title': 'N-334', 'score': 0.9875015375380549}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-567.html', 'title': 'N-567', 'score': 0.9871286998383851}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-554.html', 'title': 'N-554', 'score': 0.9864195549518338}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-694.html', 'title': 'N-694', 'score': 0.9860568599996579}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-123.html', 'title': 'N-123', 'score': 0.9858706228236708}]
result = search.search('coconut blueberry banana papaya cherry cherry apricot',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #447 checking search results for 'coconut blueberry banana papaya cherry cherry apricot' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #447 checking search results for 'coconut blueberry banana papaya cherry cherry apricot' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #448 checking search results for 'apple blueberry orange coconut peach' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-846.html', 'title': 'N-846', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-416.html', 'title': 'N-416', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-382.html', 'title': 'N-382', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-768.html', 'title': 'N-768', 'score': 0.9984981961141308}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-980.html', 'title': 'N-980', 'score': 0.9984456873548986}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-842.html', 'title': 'N-842', 'score': 0.9972959537292564}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-738.html', 'title': 'N-738', 'score': 0.9968500362920456}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-580.html', 'title': 'N-580', 'score': 0.9965310635415717}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-537.html', 'title': 'N-537', 'score': 0.9961930312959366}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-500.html', 'title': 'N-500', 'score': 0.9961411471855665}]
result = search.search('apple blueberry orange coconut peach',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #448 checking search results for 'apple blueberry orange coconut peach' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #448 checking search results for 'apple blueberry orange coconut peach' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #449 checking search results for 'coconut banana peach cherry' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-598.html', 'title': 'N-598', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-901.html', 'title': 'N-901', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-500.html', 'title': 'N-500', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-165.html', 'title': 'N-165', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-262.html', 'title': 'N-262', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-768.html', 'title': 'N-768', 'score': 0.9989388127241124}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-854.html', 'title': 'N-854', 'score': 0.9986255683150308}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-362.html', 'title': 'N-362', 'score': 0.9982013726310845}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-179.html', 'title': 'N-179', 'score': 0.9981756118126346}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-781.html', 'title': 'N-781', 'score': 0.9979321072001315}]
result = search.search('coconut banana peach cherry',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #449 checking search results for 'coconut banana peach cherry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #449 checking search results for 'coconut banana peach cherry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #450 checking search results for 'tomato lime coconut lime papaya fig apricot tomato' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-998.html', 'title': 'N-998', 'score': 0.9999555813144124}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-500.html', 'title': 'N-500', 'score': 0.9992361926360626}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-208.html', 'title': 'N-208', 'score': 0.9987503007409867}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-101.html', 'title': 'N-101', 'score': 0.9965915513915604}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-244.html', 'title': 'N-244', 'score': 0.9961057130215043}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-659.html', 'title': 'N-659', 'score': 0.9957042450662823}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-37.html', 'title': 'N-37', 'score': 0.9934637834446074}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-688.html', 'title': 'N-688', 'score': 0.9932626163882454}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-761.html', 'title': 'N-761', 'score': 0.9924455688196719}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-198.html', 'title': 'N-198', 'score': 0.9916449612253341}]
result = search.search('tomato lime coconut lime papaya fig apricot tomato',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #450 checking search results for 'tomato lime coconut lime papaya fig apricot tomato' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #450 checking search results for 'tomato lime coconut lime papaya fig apricot tomato' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #451 checking search results for 'kiwi blueberry peach pear apricot fig' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-713.html', 'title': 'N-713', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-868.html', 'title': 'N-868', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-500.html', 'title': 'N-500', 'score': 0.9980978454160266}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-560.html', 'title': 'N-560', 'score': 0.9972750911367805}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-351.html', 'title': 'N-351', 'score': 0.9946676818867508}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-967.html', 'title': 'N-967', 'score': 0.9945192667587489}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-388.html', 'title': 'N-388', 'score': 0.9940481014809855}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-360.html', 'title': 'N-360', 'score': 0.9937477484675548}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-334.html', 'title': 'N-334', 'score': 0.992524229102478}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-94.html', 'title': 'N-94', 'score': 0.9921715799596903}]
result = search.search('kiwi blueberry peach pear apricot fig',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #451 checking search results for 'kiwi blueberry peach pear apricot fig' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #451 checking search results for 'kiwi blueberry peach pear apricot fig' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #452 checking search results for 'blueberry papaya kiwi orange tomato apricot' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-416.html', 'title': 'N-416', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-713.html', 'title': 'N-713', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-637.html', 'title': 'N-637', 'score': 0.9984909107924576}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-500.html', 'title': 'N-500', 'score': 0.9980790527047301}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-90.html', 'title': 'N-90', 'score': 0.9963774452361727}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-813.html', 'title': 'N-813', 'score': 0.9949212413252707}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-453.html', 'title': 'N-453', 'score': 0.994613907946098}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-647.html', 'title': 'N-647', 'score': 0.9945818816409885}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-409.html', 'title': 'N-409', 'score': 0.9930424251125243}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-821.html', 'title': 'N-821', 'score': 0.9926225015713659}]
result = search.search('blueberry papaya kiwi orange tomato apricot',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #452 checking search results for 'blueberry papaya kiwi orange tomato apricot' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #452 checking search results for 'blueberry papaya kiwi orange tomato apricot' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #453 checking search results for 'lime apple apricot lime fig' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-6.html', 'title': 'N-6', 'score': 0.018560462511333628}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'title': 'N-0', 'score': 0.014505349941194366}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-5.html', 'title': 'N-5', 'score': 0.011644726569108725}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-25.html', 'title': 'N-25', 'score': 0.009886292435944617}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-4.html', 'title': 'N-4', 'score': 0.00932045778059954}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-64.html', 'title': 'N-64', 'score': 0.007950089796481822}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-2.html', 'title': 'N-2', 'score': 0.00635660155241577}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-3.html', 'title': 'N-3', 'score': 0.006317972646957256}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-7.html', 'title': 'N-7', 'score': 0.006120414280623874}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-41.html', 'title': 'N-41', 'score': 0.006019162176352675}]
result = search.search('lime apple apricot lime fig',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #453 checking search results for 'lime apple apricot lime fig' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #453 checking search results for 'lime apple apricot lime fig' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #454 checking search results for 'coconut orange lime fig tomato banana apple' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-635.html', 'title': 'N-635', 'score': 1.0000000000000004}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-639.html', 'title': 'N-639', 'score': 0.9961828158081025}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-959.html', 'title': 'N-959', 'score': 0.9959158411246594}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-768.html', 'title': 'N-768', 'score': 0.9955987551973545}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-541.html', 'title': 'N-541', 'score': 0.994966746195308}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-818.html', 'title': 'N-818', 'score': 0.9946877426646089}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-351.html', 'title': 'N-351', 'score': 0.9944951218373013}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-453.html', 'title': 'N-453', 'score': 0.9933965046638482}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-56.html', 'title': 'N-56', 'score': 0.9926983905537871}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-150.html', 'title': 'N-150', 'score': 0.9925236926360619}]
result = search.search('coconut orange lime fig tomato banana apple',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #454 checking search results for 'coconut orange lime fig tomato banana apple' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #454 checking search results for 'coconut orange lime fig tomato banana apple' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #455 checking search results for 'papaya pear coconut papaya blueberry' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-496.html', 'title': 'N-496', 'score': 0.9997539638459546}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-800.html', 'title': 'N-800', 'score': 0.9988846836870905}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-645.html', 'title': 'N-645', 'score': 0.9985087954671948}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-396.html', 'title': 'N-396', 'score': 0.9978405914124853}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-805.html', 'title': 'N-805', 'score': 0.9964337428976535}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-202.html', 'title': 'N-202', 'score': 0.9962534532773848}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-19.html', 'title': 'N-19', 'score': 0.9951849007397509}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-488.html', 'title': 'N-488', 'score': 0.9938856471502481}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-310.html', 'title': 'N-310', 'score': 0.9935733153735854}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-88.html', 'title': 'N-88', 'score': 0.9927998511261742}]
result = search.search('papaya pear coconut papaya blueberry',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #455 checking search results for 'papaya pear coconut papaya blueberry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #455 checking search results for 'papaya pear coconut papaya blueberry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #456 checking search results for 'fig orange cherry orange tomato pear papaya kiwi' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-990.html', 'title': 'N-990', 'score': 0.9944521346993359}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-558.html', 'title': 'N-558', 'score': 0.9936173572121388}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-369.html', 'title': 'N-369', 'score': 0.9912413988067482}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-354.html', 'title': 'N-354', 'score': 0.9909393069505257}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-279.html', 'title': 'N-279', 'score': 0.9909119039238782}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-273.html', 'title': 'N-273', 'score': 0.9897376393022177}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-229.html', 'title': 'N-229', 'score': 0.9890897562668004}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-759.html', 'title': 'N-759', 'score': 0.9880157132819075}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-967.html', 'title': 'N-967', 'score': 0.9857586916965931}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-277.html', 'title': 'N-277', 'score': 0.984441380148217}]
result = search.search('fig orange cherry orange tomato pear papaya kiwi',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #456 checking search results for 'fig orange cherry orange tomato pear papaya kiwi' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #456 checking search results for 'fig orange cherry orange tomato pear papaya kiwi' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #457 checking search results for 'apricot orange apple blueberry papaya coconut orange apricot' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-882.html', 'title': 'N-882', 'score': 0.9953772832414871}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-604.html', 'title': 'N-604', 'score': 0.9928982504730965}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-622.html', 'title': 'N-622', 'score': 0.9927686253205286}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-391.html', 'title': 'N-391', 'score': 0.992035101712487}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-511.html', 'title': 'N-511', 'score': 0.9916181193968141}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-538.html', 'title': 'N-538', 'score': 0.990554133181225}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-888.html', 'title': 'N-888', 'score': 0.9901080570318632}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-616.html', 'title': 'N-616', 'score': 0.9876154699722448}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-422.html', 'title': 'N-422', 'score': 0.9861714986225503}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-78.html', 'title': 'N-78', 'score': 0.9859022582351462}]
result = search.search('apricot orange apple blueberry papaya coconut orange apricot',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #457 checking search results for 'apricot orange apple blueberry papaya coconut orange apricot' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #457 checking search results for 'apricot orange apple blueberry papaya coconut orange apricot' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #458 checking search results for 'pear pear coconut coconut blueberry apricot' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-617.html', 'title': 'N-617', 'score': 0.9998820931219519}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-764.html', 'title': 'N-764', 'score': 0.9998264573366357}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-632.html', 'title': 'N-632', 'score': 0.9998004872810835}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-301.html', 'title': 'N-301', 'score': 0.9997738163604988}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-584.html', 'title': 'N-584', 'score': 0.9979814757896718}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-769.html', 'title': 'N-769', 'score': 0.9967182451841042}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-157.html', 'title': 'N-157', 'score': 0.9966933105285629}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-90.html', 'title': 'N-90', 'score': 0.9960298760270995}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-293.html', 'title': 'N-293', 'score': 0.9957890752236636}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-763.html', 'title': 'N-763', 'score': 0.995435938868564}]
result = search.search('pear pear coconut coconut blueberry apricot',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #458 checking search results for 'pear pear coconut coconut blueberry apricot' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #458 checking search results for 'pear pear coconut coconut blueberry apricot' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #459 checking search results for 'banana apple cherry pear apple cherry apricot' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-748.html', 'title': 'N-748', 'score': 0.9999192152396505}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-985.html', 'title': 'N-985', 'score': 0.9936598469412844}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-96.html', 'title': 'N-96', 'score': 0.9935532875980163}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-246.html', 'title': 'N-246', 'score': 0.9933928202852846}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-159.html', 'title': 'N-159', 'score': 0.9933361485125458}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-729.html', 'title': 'N-729', 'score': 0.9932217326547589}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-960.html', 'title': 'N-960', 'score': 0.9926799860642374}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-85.html', 'title': 'N-85', 'score': 0.9924281471531321}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-489.html', 'title': 'N-489', 'score': 0.9920841204965953}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-659.html', 'title': 'N-659', 'score': 0.9919592470202067}]
result = search.search('banana apple cherry pear apple cherry apricot',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #459 checking search results for 'banana apple cherry pear apple cherry apricot' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #459 checking search results for 'banana apple cherry pear apple cherry apricot' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #460 checking search results for 'banana apricot papaya banana fig lime apricot' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-34.html', 'title': 'N-34', 'score': 0.9938617739421692}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-191.html', 'title': 'N-191', 'score': 0.993029540156192}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-981.html', 'title': 'N-981', 'score': 0.9920134460861946}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-348.html', 'title': 'N-348', 'score': 0.9919454292362064}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-28.html', 'title': 'N-28', 'score': 0.9916944068672418}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-268.html', 'title': 'N-268', 'score': 0.9914640496084598}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-18.html', 'title': 'N-18', 'score': 0.9910439680221109}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-177.html', 'title': 'N-177', 'score': 0.9885153898436935}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-362.html', 'title': 'N-362', 'score': 0.988200495416108}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-968.html', 'title': 'N-968', 'score': 0.9880983105876259}]
result = search.search('banana apricot papaya banana fig lime apricot',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #460 checking search results for 'banana apricot papaya banana fig lime apricot' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #460 checking search results for 'banana apricot papaya banana fig lime apricot' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #461 checking search results for 'peach tomato cherry lime peach apple papaya tomato' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-6.html', 'title': 'N-6', 'score': 0.014179732452874105}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'title': 'N-0', 'score': 0.01254074395092133}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-5.html', 'title': 'N-5', 'score': 0.012471616394511418}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-25.html', 'title': 'N-25', 'score': 0.010447464033631603}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-4.html', 'title': 'N-4', 'score': 0.007869060229981765}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-2.html', 'title': 'N-2', 'score': 0.006579382693043231}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-7.html', 'title': 'N-7', 'score': 0.006543182889411724}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-3.html', 'title': 'N-3', 'score': 0.006370461467050376}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-241.html', 'title': 'N-241', 'score': 0.006197901715487629}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-64.html', 'title': 'N-64', 'score': 0.006197143230303812}]
result = search.search('peach tomato cherry lime peach apple papaya tomato',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #461 checking search results for 'peach tomato cherry lime peach apple papaya tomato' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #461 checking search results for 'peach tomato cherry lime peach apple papaya tomato' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


output.close()
success_output.close()







output.close()
success_output.close()
