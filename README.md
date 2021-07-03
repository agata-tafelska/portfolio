# Projekt zaliczeniowy z przedmiotu "Programowanie i architektura aplikacji w chmurze"
Repozytorium zawiera kod źródłowy przykładowej aplikacji "Portfolio" składającej się ze strony głównej i kilku tematycznych podstron.
Do głównych funkcjonalności należą:
* zaimplementowana strona główna z karuzelą zdjęć
* przykładowa galeria zdjęć z możliwością przybliżenia wybranego zdjęcia
* księga gości z możliwością dodania wpisu
* strona kontaktowa z formularzem wysyłania emaila

## Detale techniczne
Projekt został napisany z wykorzystaniem następujących technologii:
* język programowania `Python`
* framework aplikacji webowych `Flask`
* interfejs do obsługi bazy danych `pypyobdc`
* dodatkowe biblioteki rozszerzające (dokładny spis znajduje się w pliku [requirements.txt](requirements.txt)

Projekt wykorzystuje bazę danych do której dostęp przekazywany jest przez zmienne środowiskowe podczas uruchamiania aplikacji.

Projekt wdrożony jest z wykorzystaniem usługi App Service dostępnej na platformie Azure.
Do ciągłej integracji i wdrażania wykorzystywane są `Gihub Actions`, które budują i wdrażają kolejną wersję projektu na każdy nowy commit na gałęzi `main`.
