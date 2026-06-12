```mermaid
erDiagram

user {
    int id pk
    int nama
}

pendidikan {
    int id pk
    str nim uk
    
}

user ||--|{ pendidikan : ""

```