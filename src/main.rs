use reqwest::get;
use serde::Deserialize;
use std::fs;

#[derive(Deserialize)]
struct Quote {
    quote: String,
    author: String,
}

async fn fetch_quote() -> Result<Quote, reqwest::Error> {
    let response = get("https://quotes-api-self.vercel.app/quote").await?;
    let quote: Quote = response.json::<Quote>().await?;
    Ok(quote)
}

async fn write_quote_to_readme(quote: Quote) -> std::io::Result<()> {
    let content = format!("<i> {} </i>\n\n{}", quote.quote, quote.author);
    fs::write("README.md", content)
}

#[tokio::main]
async fn main() {
    let quote: Quote = fetch_quote().await.unwrap();
    write_quote_to_readme(quote).await.unwrap();
}
