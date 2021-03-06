# Pizzapalvelu

Kuvaus sisältää suluissa toiminnot, joita ei vielä toteutettu.

Eräs pizzapalvelu on suunnittelemassa toimintaansa varten tietojärjestelmää. Asiakas tekee tilauksensa internetin välityksellä. Tilaus 
voi käsittää useita tuotteita. Pizzoja on muutamaa perustyyppiä, (joita voi täydentää erilaisilla lisukkeilla). Valikoima (ja lisukkeet)
 sekä niiden hinnat muuttuvat aika ajoin. (Pizzojen lisäksi tarjolla on myös juomia.) 

(Tuotteet on luokiteltu tuoteryhmiin.) Kaikista tuotteista on olemassa tekstikuvaus ja osasta myös kuva. (Tuotteen hinta voi vaihdella 
esim. vuorokauden eri aikoina.) Laskutuksessa käytetään tilausajankohtana voimassaolleen hinnaston toimitusajankohdalle kiinittämää hintaa. 
Kuhunkin toimitukseen liittyen laaditaan laskelma, jonka mukaisesti hinta peritään.

Tilauksen yhteydessä sovitaan (toimitusaika ja) toimitusosoite. Asiakas identifioidaan nimellä ja puhelin- tms. yhteystunnuksella. 
Toimituksista kirjataan suoritusaika, ja löytyikö asiakas sekä liittyikö toimitukseen jotain häiriöitä. 
Jos tietyyn osoitteeseen toimitukseen on liittynyt häiriöitä yritys voi evätä tilauksen. (Asiakas voi perua tai muuttaa tilaustaan, jos 
sovituun toimitukseen on aikaa yli tunti.)

Toimintoja:
* tuotetietojen lisäys, muokkaus ja poisto menusta.
* tuotteiden selailu.
* asiakkaan lisäys, tilausstatuksen muokkaus ja poisto
* tilauksen laatiminen, muokkaus ja poisto.
* toimituksen kirjaus.
* tilauslistan tarkastelu sekä kaikkien, että ei toimitettujen tilausten osalta.
* kuitin tulostus.
* tilaussstatistiikan tarkastelu.
* ylläpidon kirjautuminen ja tilauksen tehneen asiakkaan tunnistaminen/kirjautuminen.

***

## Linkit 

[Linkki Herokuun](https://pizzapalvelu.herokuapp.com)


[User Storyt](/documentation/user_stories)


[Tietokantakaavio](/documentation/Tietokantakaavio.png)

[Käyttö-ja asennusohje](/documentation/kaytto_ja_asennusohje)

[Create table-lauseet](/documentation/CreateTable_lauseet)

***

Testitunnukset voi luoda yläpalkin Register new user-kohdassa. 
Voit myös käyttää valmiita tunnuksia. Käyttäjätason tunnukset: username "testi" ja salasana "testi123".
Admin-tason tunnukset: username "admin" ja salasana "admin123".
