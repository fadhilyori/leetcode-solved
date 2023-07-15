# Write your MySQL query statement below

SELECT
    t.request_at AS Day,
    ROUND(
        SUM(CASE 
            WHEN t.status <> 'completed' THEN 1
            ELSE 0
        END) / COUNT(*),
        2
    ) AS 'Cancellation Rate'
FROM
    Trips t
JOIN
    Users c ON t.client_id = c.users_id AND c.banned = 'No'
JOIN
    Users d ON t.driver_id = d.users_id AND d.banned = 'No'
WHERE
    t.request_at BETWEEN '2013-10-01' AND '2013-10-03'
GROUP BY
    t.request_at
