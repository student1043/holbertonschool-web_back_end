-- Task 3
-- MySQL Project
SELECT band_name, (IFNULL(split, 2020) - formed) AS lifespan FROM metal_bands
                        WHERE style LIKE '%Glam rock%' ORDER BY lifespan DESC;
