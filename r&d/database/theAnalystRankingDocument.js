//theAnalystRankingDocument
{
	_id : "blah",
	"authorName" : "John Sandoz",
	// "authorID" : 12 // autoincrement upon addition
	"overallRating" : 3.8 //1 thru 5
	"industrySpecificRating" : 
	{
		{ "industry" : "HealthCare", "rating" : 3.1},
		{ "industry" : "IT", "rating" : 4.5}

	},
	"individualStockRating" :  // this section get populated after the prediction time frame for stock has elapsed and we can compare actual vs predicated price.
	{
		{ "stockSymbol": "CSCO", "rating" : 4.6},
		{ "stockSymbol" : "ORCL", "rating" : 4.4 }
		{ "stockSymbol": "HCA", "rating" : 3.3},
		{ "stockSymbol": "BIO", "rating" : 2.9}
	}

}