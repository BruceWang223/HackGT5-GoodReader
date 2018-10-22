from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types

from google.cloud import texttospeech

from gensim.summarization.summarizer import summarize

import nltk
# from nltk import word_tokenize
# from nltk import pos_tag
import string

import json

import cloudinary as Cloud
import cloudinary.uploader
import cloudinary.api

class NLP:
	def __init__(self, rawString):
		self.rawContent = rawString
		self.client = language.LanguageServiceClient()
		self.speechClient = texttospeech.TextToSpeechClient()

		self.numOfTopics = 5
		self.numOfEntities = 20
		self.lengthOfSummary = 100

		self.cleanText()

	# Potential Improvement: multi-threading for the function
	# one thread to get Google API, the ther to get normal NLP result locally
	def getInsight(self):
		insight = {}
		insight['summarization'] = self.getSummarization()
		googleResult = self.getAllGoogleNLPResult()
		insight['topics'] = googleResult["categories"]
		insight["entities"] = googleResult["entities"]

		self.insight = insight

		googleKeywords = [ele["name"] for ele in insight["entities"]]
		self.cleanUp()

		self.insight["keywords"] = self.annotateKeywordsGoogle()

		audioURL = self.synthesisSummaryAudio()
		self.insight["url"] = audioURL

		return json.dumps(self.insight)

	def synthesisSummaryAudio(self):
		textForSynthesis = self.insight["summarization"].replace("\n", " ").replace("\t", " ")
		input_text = texttospeech.types.SynthesisInput(text = textForSynthesis)
		voice = texttospeech.types.VoiceSelectionParams(
			language_code='en-US',
			ssml_gender=texttospeech.enums.SsmlVoiceGender.FEMALE)

		audio_config = texttospeech.types.AudioConfig(
			audio_encoding=texttospeech.enums.AudioEncoding.MP3)

		response = self.speechClient.synthesize_speech(input_text, voice, audio_config)

		with open("summary.mp3", "wb") as out:
			out.write(response.audio_content)

		out.close()

		Cloud.config(
			#put your own api key inside
		)
		temp =  Cloud.uploader.upload('summary.mp3', resource_type='raw')
		print temp["url"]

		return temp["url"]

	def getAllGoogleNLPResult(self):
		result = {}
		document = types.Document(
			content = self.rawContent,
			type = enums.Document.Type.PLAIN_TEXT)

		entities = self.client.analyze_entities(document).entities

		# entity types from enums.Entity.Type
		entity_type = ('UNKNOWN', 'PERSON', 'LOCATION', 'ORGANIZATION',
						'EVENT', 'WORK_OF_ART', 'CONSUMER_GOOD', 'OTHER')

		# available entity metadata: wikipedia urls, and knowledge graph IDs, if these are available
		# assume entities are returned in the order of salience value DESC

		result["entities"] = []
		for entity in entities:
			entityName = str(entity.name.encode('utf-8'))
			entityType = str(entity_type[entity.type])
			entitySalience = entity.salience
			entityUrl = "{}".format(entity.metadata.get('wikipedia_url', '-').encode('utf-8'))

			result["entities"].append({"name": entityName, "type": entityType, "salience": entitySalience, "wikipedia_url": entityUrl})

		# result["entities"] = [{"name": str(entity.name), "type": str(entity_type[entity.type]), 'salience': entity.salience, \
		# 	'wikipedia_url': str(entity.metadata.get('wikipedia_url', '-'))} for entity in entities]

		# result["entities"] = result["entities"][:10]

		categories = self.client.classify_text(document).categories

		result["categories"] = []
		for category in categories:
			entries = str(category.name).split("/")[1:]
			categoryName = " - ".join(entries)
			result["categories"].append({"name": categoryName, "confidence": category.confidence})

		# result["categories"] = result["categories"][:5]

		return result

	def getSummarization(self):
		return summarize(text = str(self.rawContent.encode('utf-8')), word_count = self.lengthOfSummary)

	def getRAKEKeyphrase(self):
		return

	def getTextRank(self):
		return

	def annotateKeywords(self, googleKeywords):
		preprocessing = str(self.insight["summarization"])
		text = preprocessing.translate(None, string.punctuation)
		# tagContent = str(tagContent.encode('utf-8')).translate(None, string.punctuation)
		# tokens = word_tokenize(sentence)
		# tagged = pos_tag(tokens)
		tokens = nltk.word_tokenize(text)
		tagged = nltk.pos_tag(tokens)
		grammar = "NP:{<DT>?<JJ|NN|NNS>*<NN|NNS>}"
		cp = nltk.RegexpParser(grammar)
		resultTree = cp.parse(tagged)
		result = []
		for node in resultTree:
			# print node
			if (type(node) == nltk.tree.Tree):
				# currNounPhrase = ''.join(stemmer.stem(item[0]) for item in node.leaves())
				currNP = " ".join(str(item[0].encode('utf-8')) for item in node.leaves())
				result.append(currNP)
			else:
				result.append(str(node[0].encode('utf-8')))
		
		result = [ele for ele in result if ele in googleKeywords]
		return result

	def annotateKeywordsGoogle(self):
		# preprocessing = str(self.insight["summarization"])
		preprocessing = "".join([c for c in str(self.insight["summarization"]) if c.isalpha() or c == " "])
		result = [ele["name"] for ele in self.insight["entities"] if ele["name"] in preprocessing]
		return result

	def cleanText(self):
		self.rawContent = self.rawContent.decode('utf-8')
		return

	def cleanUp(self):
		categories = self.insight["topics"]
		entities = self.insight["entities"]

		self.insight["topics"] = categories[:self.numOfTopics]
		self.insight["entities"] = entities[:self.numOfEntities]
		return
