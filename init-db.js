db = db.getSiblingDB("eagle_db");
db.eagle_tb.drop();

db.eagle_tb.insertMany([
    {
        "id": 1,
        "name": "Serpent Eagles",
        "description": "These are the most common eagles that belong to Asia and African continents. The serpent eagles are popular species that hunt and go after reptiles and snakes. These eagles come with very sharp and powerful beaks, clear and distant vision, and are silent too. These characteristics of being sharp, clear, powerful in nature make them distinct from other species in being excellent hunters. They aren’t, however, enormous like other species of eagles when compared."
    },
    {
        "id": 2,
        "name": "Hawk Eagles",
        "description": "The name Hawk eagles have come to them, given their resemblance to hawks. However, these are very different from hawks; their population is heavier in tropical areas, around South America, Asia, and Africa. They have distinct crests near heads, medium in size. The popular hawk eagles include a martial eagle, one among the largest of the species."
    },
    {
        "id": 3,
        "name": "True Eagles",
        "description": "The types of true eagles are found in India mostly, along with countries in Asia and Africa. They have strong long feathered legs that can extend till the feet and come with heavy beaks, head appearances, and hooked. They generally look larger than other types of eagles. The common and popular true eagles are spotted eagles and tawny eagles."
    },
    {
        "id": 4,
        "name": "Sea Eagles",
        "description": "The sea eagles are among the largest species of eagles now. These eagles survive near large water bodies and feed on waterfowl, fishes, and snails. They are quite the oldest eagles, and history tells us that these same eagles species even existed over 12 million years ago. The famous sea eagle kind includes the Steller sea eagle in Asia."
    },
]);