
import testingtools
import crawler
import searchdata
import search
output = open('fruits5-tfidf-failed.txt', 'w')
success_output = open('fruits5-tfidf-passed.txt', 'w')

#Performing crawl starting at seed http://people.scs.carleton.ca/~davidmckenney/fruits5/N-0.html
crawler.crawl('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-0.html')
#Test #0 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-35.html and word blueberry
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-35.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #0 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-35.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #0 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-35.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #1 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-35.html and word apple
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-35.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #1 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-35.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #1 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-35.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #2 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-35.html and word lime
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-35.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #2 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-35.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #2 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-35.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #3 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-35.html and word banana
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-35.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #3 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-35.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #3 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-35.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #4 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-35.html and word peach
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-35.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #4 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-35.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #4 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-35.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #5 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-35.html and word cherry
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-35.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #5 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-35.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #5 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-35.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #6 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-35.html and word orange
expected = 0.16650266314016507
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-35.html','orange')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #6 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-35.html and word orange\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #6 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-35.html and word orange\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #7 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-35.html and word apricot
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-35.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #7 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-35.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #7 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-35.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #8 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-35.html and word coconut
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-35.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #8 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-35.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #8 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-35.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #9 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-35.html and word kiwi
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-35.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #9 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-35.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #9 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-35.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #10 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-35.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-35.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #10 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-35.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #10 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-35.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #11 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-158.html and word blueberry
expected = 0.012639539873791985
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-158.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #11 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-158.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #11 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-158.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #12 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-158.html and word apple
expected = 0.014087948176820598
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-158.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #12 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-158.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #12 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-158.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #13 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-158.html and word lime
expected = 0.02876077958061864
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-158.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #13 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-158.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #13 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-158.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #14 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-158.html and word banana
expected = 0.03411432406916046
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-158.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #14 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-158.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #14 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-158.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #15 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-158.html and word peach
expected = 0.017324837275400434
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-158.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #15 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-158.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #15 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-158.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #16 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-158.html and word cherry
expected = 0.019685766704504466
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-158.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #16 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-158.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #16 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-158.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #17 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-158.html and word orange
expected = 0.006159634066546383
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-158.html','orange')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #17 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-158.html and word orange\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #17 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-158.html and word orange\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #18 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-158.html and word apricot
expected = 0.015701879791040773
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-158.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #18 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-158.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #18 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-158.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #19 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-158.html and word coconut
expected = 0.0145261422879701
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-158.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #19 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-158.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #19 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-158.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #20 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-158.html and word kiwi
expected = 0.018727099522009027
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-158.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #20 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-158.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #20 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-158.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #21 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-158.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-158.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #21 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-158.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #21 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-158.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #22 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-398.html and word blueberry
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-398.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #22 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-398.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #22 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-398.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #23 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-398.html and word apple
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-398.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #23 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-398.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #23 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-398.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #24 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-398.html and word lime
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-398.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #24 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-398.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #24 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-398.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #25 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-398.html and word banana
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-398.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #25 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-398.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #25 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-398.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #26 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-398.html and word peach
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-398.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #26 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-398.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #26 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-398.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #27 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-398.html and word cherry
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-398.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #27 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-398.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #27 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-398.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #28 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-398.html and word orange
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-398.html','orange')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #28 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-398.html and word orange\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #28 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-398.html and word orange\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #29 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-398.html and word apricot
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-398.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #29 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-398.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #29 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-398.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #30 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-398.html and word coconut
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-398.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #30 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-398.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #30 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-398.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #31 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-398.html and word kiwi
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-398.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #31 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-398.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #31 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-398.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #32 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-398.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-398.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #32 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-398.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #32 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-398.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #33 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-203.html and word blueberry
expected = 0.009600320972773082
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-203.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #33 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-203.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #33 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-203.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #34 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-203.html and word apple
expected = 0.008613543483019261
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-203.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #34 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-203.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #34 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-203.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #35 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-203.html and word lime
expected = 0.026198733188798045
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-203.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #35 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-203.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #35 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-203.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #36 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-203.html and word banana
expected = 0.01778548820997657
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-203.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #36 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-203.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #36 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-203.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #37 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-203.html and word peach
expected = 0.00888146071149114
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-203.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #37 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-203.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #37 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-203.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #38 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-203.html and word cherry
expected = 0.012931725010935684
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-203.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #38 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-203.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #38 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-203.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #39 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-203.html and word orange
expected = 0.022466134420721273
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-203.html','orange')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #39 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-203.html and word orange\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #39 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-203.html and word orange\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #40 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-203.html and word apricot
expected = 0.023342006476833172
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-203.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #40 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-203.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #40 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-203.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #41 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-203.html and word coconut
expected = 0.02159418565684508
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-203.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #41 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-203.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #41 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-203.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #42 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-203.html and word kiwi
expected = 0.03636640004600181
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-203.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #42 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-203.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #42 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-203.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #43 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-203.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-203.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #43 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-203.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #43 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-203.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #44 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-894.html and word blueberry
expected = 0.028779001097183593
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-894.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #44 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-894.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #44 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-894.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #45 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-894.html and word apple
expected = 0.019068921384461226
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-894.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #45 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-894.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #45 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-894.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #46 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-894.html and word lime
expected = 0.012735307853409157
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-894.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #46 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-894.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #46 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-894.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #47 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-894.html and word banana
expected = 0.017642689892260848
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-894.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #47 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-894.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #47 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-894.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #48 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-894.html and word peach
expected = 0.005074698990999754
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-894.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #48 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-894.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #48 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-894.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #49 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-894.html and word cherry
expected = 0.026088340415356293
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-894.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #49 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-894.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #49 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-894.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #50 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-894.html and word orange
expected = 0.01298762597983467
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-894.html','orange')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #50 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-894.html and word orange\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #50 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-894.html and word orange\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #51 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-894.html and word apricot
expected = 0.018693686633278812
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-894.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #51 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-894.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #51 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-894.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #52 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-894.html and word coconut
expected = 0.017293926302803117
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-894.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #52 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-894.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #52 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-894.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #53 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-894.html and word kiwi
expected = 0.028779001097183593
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-894.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #53 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-894.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #53 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-894.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #54 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-894.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-894.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #54 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-894.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #54 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-894.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #55 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-378.html and word blueberry
expected = 0.023054308955641093
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-378.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #55 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-378.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #55 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-378.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #56 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-378.html and word apple
expected = 0.013999840947541387
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-378.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #56 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-378.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #56 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-378.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #57 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-378.html and word lime
expected = 0.014726408617933853
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-378.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #57 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-378.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #57 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-378.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #58 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-378.html and word banana
expected = 0.014726408617933853
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-378.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #58 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-378.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #58 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-378.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #59 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-378.html and word peach
expected = 0.021328030573227835
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-378.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #59 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-378.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #59 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-378.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #60 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-378.html and word cherry
expected = 0.03383059700598984
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-378.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #60 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-378.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #60 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-378.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #61 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-378.html and word orange
expected = 0.015018175403175633
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-378.html','orange')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #61 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-378.html and word orange\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #61 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-378.html and word orange\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #62 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-378.html and word apricot
expected = 0.030288948026653693
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-378.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #62 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-378.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #62 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-378.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #63 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-378.html and word coconut
expected = 0.007330441380185931
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-378.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #63 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-378.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #63 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-378.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #64 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-378.html and word kiwi
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-378.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #64 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-378.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #64 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-378.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #65 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-378.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-378.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #65 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-378.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #65 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-378.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #66 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-260.html and word blueberry
expected = 0.02052478488367052
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-260.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #66 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-260.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #66 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-260.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #67 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-260.html and word apple
expected = 0.012443452264326808
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-260.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #67 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-260.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #67 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-260.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #68 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-260.html and word lime
expected = 0.006635532254893697
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-260.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #68 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-260.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #68 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-260.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #69 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-260.html and word banana
expected = 0.006635532254893697
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-260.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #69 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-260.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #69 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-260.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #70 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-260.html and word peach
expected = 0.03653226295055268
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-260.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #70 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-260.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #70 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-260.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #71 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-260.html and word cherry
expected = 0.006373480469039989
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-260.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #71 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-260.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #71 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-260.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #72 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-260.html and word orange
expected = 0.013348576560758857
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-260.html','orange')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #72 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-260.html and word orange\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #72 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-260.html and word orange\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #73 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-260.html and word apricot
expected = 0.013868988527476877
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-260.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #73 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-260.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #73 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-260.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #74 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-260.html and word coconut
expected = 0.018987914161735772
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-260.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #74 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-260.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #74 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-260.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #75 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-260.html and word kiwi
expected = 0.013868988527476877
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-260.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #75 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-260.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #75 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-260.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #76 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-260.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-260.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #76 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-260.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #76 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-260.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #77 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-869.html and word blueberry
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-869.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #77 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-869.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #77 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-869.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #78 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-869.html and word apple
expected = 0.01948398085514879
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-869.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #78 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-869.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #78 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-869.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #79 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-869.html and word lime
expected = 0.020495165955961167
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-869.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #79 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-869.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #79 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-869.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #80 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-869.html and word banana
expected = 0.05680471390921831
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-869.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #80 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-869.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #80 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-869.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #81 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-869.html and word peach
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-869.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #81 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-869.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #81 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-869.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #82 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-869.html and word cherry
expected = 0.03779491661309501
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-869.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #82 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-869.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #82 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-869.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #83 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-869.html and word orange
expected = 0.040128490405731757
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-869.html','orange')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #83 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-869.html and word orange\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #83 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-869.html and word orange\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #84 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-869.html and word apricot
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-869.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #84 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-869.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #84 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-869.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #85 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-869.html and word coconut
expected = 0.020090014151503705
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-869.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #85 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-869.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #85 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-869.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #86 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-869.html and word kiwi
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-869.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #86 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-869.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #86 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-869.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #87 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-869.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-869.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #87 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-869.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #87 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-869.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #88 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-594.html and word blueberry
expected = 0.008095117369539639
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-594.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #88 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-594.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #88 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-594.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #89 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-594.html and word apple
expected = 0.025552767480500196
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-594.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #89 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-594.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #89 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-594.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #90 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-594.html and word lime
expected = 0.02221448612878433
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-594.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #90 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-594.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #90 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-594.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #91 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-594.html and word banana
expected = 0.012599036042921619
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-594.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #91 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-594.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #91 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-594.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #92 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-594.html and word peach
expected = 0.017110753338439387
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-594.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #92 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-594.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #92 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-594.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #93 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-594.html and word cherry
expected = 0.01906336302548
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-594.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #93 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-594.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #93 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-594.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #94 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-594.html and word orange
expected = 0.015337925954757475
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-594.html','orange')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #94 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-594.html and word orange\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #94 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-594.html and word orange\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #95 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-594.html and word apricot
expected = 0.010736174522866506
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-594.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #95 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-594.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #95 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-594.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #96 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-594.html and word coconut
expected = 0.0025234077341478277
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-594.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #96 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-594.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #96 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-594.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #97 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-594.html and word kiwi
expected = 0.018495687755779876
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-594.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #97 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-594.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #97 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-594.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #98 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-594.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-594.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #98 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-594.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #98 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-594.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #99 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-833.html and word blueberry
expected = 0.019976864637262157
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-833.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #99 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-833.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #99 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-833.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #100 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-833.html and word apple
expected = 0.01210697658820754
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-833.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #100 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-833.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #100 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-833.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #101 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-833.html and word lime
expected = 0.024817228830548887
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-833.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #101 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-833.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #101 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-833.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #102 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-833.html and word banana
expected = 0.024817228830548887
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-833.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #102 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-833.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #102 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-833.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #103 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-833.html and word peach
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-833.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #103 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-833.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #103 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-833.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #104 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-833.html and word cherry
expected = 0.018109149908590503
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-833.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #104 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-833.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #104 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-833.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #105 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-833.html and word orange
expected = 0.01298762597983467
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-833.html','orange')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #105 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-833.html and word orange\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #105 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-833.html and word orange\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #106 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-833.html and word apricot
expected = 0.019976864637262157
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-833.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #106 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-833.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #106 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-833.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #107 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-833.html and word coconut
expected = 0.024326637777813055
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-833.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #107 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-833.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #107 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-833.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #108 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-833.html and word kiwi
expected = 0.00683816945309014
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-833.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #108 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-833.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #108 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-833.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #109 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-833.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-833.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #109 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-833.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #109 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-833.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #110 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word blueberry
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #110 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #110 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #111 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word apple
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #111 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #111 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #112 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word lime
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #112 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #112 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #113 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word banana
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #113 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #113 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #114 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word peach
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #114 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #114 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #115 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word cherry
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #115 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #115 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #116 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word orange
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','orange')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #116 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word orange\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #116 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word orange\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #117 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word apricot
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #117 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #117 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #118 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word coconut
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #118 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #118 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #119 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word kiwi
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #119 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #119 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #120 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #120 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #120 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


output.close()
success_output.close()
