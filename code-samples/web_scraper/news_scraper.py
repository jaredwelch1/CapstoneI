import newspaper

url = input('Enter a news site homepage url to scrape (e.g. http://cnn.com): ')
print ('\nBuilding newspaper tree...\n')
paper = newspaper.build(url, memoize_articles=False)

total = paper.size()


outputFile = input('Enter name of output file to append to (only .txt filetypes for now): ')


file = open(outputFile,'a+', encoding='utf8')

print('\nTotal number of articles available to process: ' + str(total) + '\n')
numScraped = input('\nEnter the number of articles to scrape (a number < total or "all" for all of them): ')

if(numScraped == 'all'):
	numScraped = total

numScraped = int(numScraped)

x = 0

for x in range(0,numScraped):
	if paper.articles[x] != None:
		file.write('\n====Article #' + str(x) + '====\n')
		paper.articles[x].download()
		if paper.articles[x].is_downloaded:
			if(paper.articles[x].html != None):
				paper.articles[x].parse()
			if paper.articles[x].title != None:
				file.write('*TITLE: ' + paper.articles[x].title)
				file.write('\n')
			if paper.articles[x].url != None:
				file.write('*URL: ' + paper.articles[x].url)
				file.write('\n')
			if paper.articles[x].authors != None:
				file.write('*AUTHORS: ' + str(paper.articles[x].authors))
				file.write('\n')
			if paper.articles[x].text != None:
				file.write('*ARTICLE: ' + paper.articles[x].text)
				print ('Article ' + str(x) + ' done\n')
			file.write('\n====End Article====\n')

file.close()
