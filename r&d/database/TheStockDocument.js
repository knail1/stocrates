//the stock document:
{
	"_id" : "xyz",
	"stockSymbol" : "CSCO",
	"companyName" : "Cisco Systems",
	"industry" : "IT",
	"Predictions" : [
	{
		"nameOfAuthor" : "JoeAnalyst", // this can be analyst or author or both 
		"nameOfQuotedAnalyst" : "Billy Bob"
		"nameOfQuotedFirm" : "Charles Schnawb Investors"
		"source" : "Barrons"
		"dateWhenPredicted" : "8/8/2013" 
		"futurePredictedDate" : "6/6/2016", // bson date time (check blog project, ISODate("2012-11-20T05:05:15.229Z")) if future date doesn't exist this was a sh*tty recommendation, rate the analyst accordingly
		"futurePredictedPrice" : 46, // if future price doesn't exist this was an even more sh*tty recommendation, rate analyst accordingly
		"wasDateCalculated" : 1 // 1 is yes calculated by stAR, 0 is no, the analyst provided this date
		"wasPriceCalculated" : 1 // 1 is yes, 0 is no
		"futureDateRangeInWeeks" : 10  // +/- 10 weeks, tighter the range, higher the rating, proportional to price point (STDDEV)
		"futurePriceRangeInDollars" : 3 // +/- $$ , tighter the range, higher the rating, proportional to price point (STDDEV)
		"proof" : bsonBinary // bsonBinaryfield for jpg
		"notes" : "open text notes blah blah"
		// "numberOfThumbsUp" : 255
		// "numberOfThumbsDown" : 40
	},
	{
		"nameOfPredictor" : "JaneGizmodo", // this can be analyst or author or both
		"nameOfQuotedAnalyst" : "Billy Bob"
		"nameOfQuotedFirm" : "Charles Schnawb Investors"
		"source" : "Barrons"
		"dateWhenPredicted" : "3/4/2013" 
		"futurePredictedDate" : "3/6/2016", // bson date time, if future date doesn't exist this was a sh*tty recommendation, rate the analyst accordingly
		"futurePredictedPrice" : 26, // if future price doesn't exist this was an even more sh*tty recommendation, rate analyst accordingly
		"wasDateCalculated" : 1 // 1 is yes calculated by stAR, 0 is no, the analyst provided this date
		"wasPriceCalculated" : 0 // 1 is yes it was calculated by stAR, 0 is no, it was precisely provided by analyst
		"futureDateRangeInWeeks" : 10  // +/- 10 weeks, tighter the range, higher the rating, proportional to price point (STDDEV)
		"futurePriceRangeInDollars" : 3 // +/- $$ , tighter the range, higher the rating, proportional to price point (STDDEV)
		"proof" : bsonBinary // bsonBinaryfield for jpg
		"notes" : "open text notes blah blah"
		// "numberOfThumbsUp" : 255
		// "numberOfThumbsDown" : 40
	},
	{
		"nameOfPredictor" : "TrentReznor", // this can be analyst or author or both
		"nameOfQuotedAnalyst" : "Billy Bob"
		"nameOfQuotedFirm" : "Charles Schnawb Investors"
		"source" : "Barrons"
		"dateWhenPredicted" : "3/4/2013" 
		"futurePredictedDate" : "3/6/2016", // bson date time, if future date doesn't exist this was a sh*tty recommendation, rate the analyst accordingly
		"futurePredictedPrice" : 96, // if future price doesn't exist this was an even more sh*tty recommendation, rate analyst accordingly
		"wasDateCalculated" : 0 // 1 is yes calculated by stAR, 0 is no, the analyst provided this date
		"wasPriceCalculated" : 1 // 1 is yes it was calculated by stAR, 0 is no, it was precisely provided by analyst
		"futureDateRangeInWeeks" : 5  // +/- 10 weeks, tighter the range, higher the rating, proportional to price point (STDDEV)
		"futurePriceRangeInDollars" : 10 // +/- $$ , tighter the range,  higher the rating, proportional to price point (STDDEV)
		"proof" : bsonBinary // bsonBinaryfield for jpg
		"notes" : "open text notes blah blah"
		// "numberOfThumbsUp" : 255
		// "numberOfThumbsDown" : 40
	}

		
		]

	]


}