# BookingGuard data dictionary

Each row is one hotel booking evaluated before arrival. `canceled` appears only in training data.

| Field | Meaning |
|---|---|
| `booking_id` | Random course identifier |
| `hotel` | Resort or city hotel |
| `lead_time` | Days between booking and scheduled arrival |
| `arrival_year`, `arrival_week`, `arrival_month`, `arrival_day` | Scheduled arrival timing |
| `weekend_nights`, `weekday_nights` | Planned length of stay |
| `adults`, `children`, `babies` | Party composition |
| `meal` | Booked meal package |
| `country` | Country code associated with booking |
| `market_segment`, `distribution_channel` | Commercial source/channel |
| `repeated_guest` | Prior-guest indicator |
| `previous_cancellations` | Earlier cancellations by customer |
| `previous_completed_bookings` | Earlier completed bookings |
| `room_type` | Reserved room category |
| `booking_changes` | Changes recorded by the decision point |
| `deposit_type` | Existing deposit arrangement |
| `waitlist_days` | Days spent on waiting list |
| `customer_type` | Contract/transient customer category |
| `average_daily_rate` | Average daily booking rate |
| `parking_spaces` | Requested parking spaces |
| `special_requests` | Number of special requests |
| `canceled` | Binary training target |

Blank country or child counts are genuine missing values. Encoded categories are intentionally not expanded into natural-language names.
