

Item_Index : 0
Start Commercial
data: list[object] 
 length: int 
 message: str 
 retry_after: int 
 

Item_Index : 1
Get Extension Analytics
data: list[object] 
 extension_id: str 
 URL: str 
 type: str 
 date_range: object 
 started_at: str 
 ended_at: str 
 pagination: object 
 cursor: str 
 

Item_Index : 2
Get Game Analytics
data: list[object] 
 game_id: str 
 URL: str 
 type: str 
 date_range: object 
 started_at: str 
 ended_at: str 
 pagination: object 
 cursor: str 
 

Item_Index : 3
Get Bits Leaderboard
data: list[object] 
 user_id: str 
 user_login: str 
 user_name: str 
 rank: int 
 score: int 
 date_range: object 
 started_at: str 
 ended_at: str 
 total: int 
 

Item_Index : 4
Get Cheermotes
data: list[object] 
 prefix: str 
 tiers: list[object] 
 min_bits: int 
 id: str 
 color: str 
 images: dict 
 can_cheer: bool 
 show_in_bits_card: bool 
 type: str 
 order: int 
 last_updated: str 
 is_charitable: bool 
 

Item_Index : 5
Get Extension Transactions
data: list[object] 
 id: str 
 timestamp: str 
 broadcaster_id: str 
 broadcaster_login: str 
 broadcaster_name: str 
 user_id: str 
 user_login: str 
 user_name: str 
 product_type: str 
 product_data: object 
 sku: str 
 domain: str 
 cost: object 
 amount: int 
 type: str 
 inDevelopment: bool 
 displayName: str 
 expiration: str 
 broadcast: bool 
 pagination: object 
 cursor: str 
 

Item_Index : 6
Get Channel Information
data: list[object] 
 broadcaster_id: str 
 broadcaster_login: str 
 broadcaster_name: str 
 broadcaster_language: str 
 game_name: str 
 game_id: str 
 title: str 
 delay: None 
 tags: list[str] 
 game_id: str 
 broadcaster_language: str 
 title: str 
 delay: int 
 tags: list[str] 
 

Item_Index : 8
Get Channel Editors
data: list[object] 
 user_id: str 
 user_name: str 
 created_at: str 
 

Item_Index : 9
Get Followed Channels
data: list[object] 
 broadcaster_id: str 
 broadcaster_login: str 
 broadcaster_name: str 
 followed_at: str 
 pagination: object 
 cursor: str 
 total: int 
 

Item_Index : 10
Get Channel Followers
data: list[object] 
 followed_at: str 
 user_id: str 
 user_login: str 
 user_name: str 
 pagination: object 
 cursor: str 
 total: int 
 

Item_Index : 11
Create Custom Rewards
data: list[object] 
 broadcaster_id: str 
 broadcaster_login: str 
 broadcaster_name: str 
 id: str 
 title: str 
 prompt: str 
 cost: int 
 image: object 
 url_1x: str 
 url_2x: str 
 url_4x: str 
 default_image: object 
 url_1x: str 
 url_2x: str 
 url_4x: str 
 background_color: str 
 is_enabled: bool 
 is_user_input_required: bool 
 max_per_stream_setting: object 
 is_enabled: bool 
 max_per_stream: None 
 max_per_user_per_stream_setting: object 
 is_enabled: bool 
 max_per_user_per_stream: None 
 global_cooldown_setting: object 
 is_enabled: bool 
 global_cooldown_seconds: None 
 is_paused: bool 
 is_in_stock: bool 
 should_redemptions_skip_request_queue: bool 
 redemptions_redeemed_current_stream: int 
 cooldown_expires_at: str 
 

Item_Index : 13
Get Custom Reward
data: list[object] 
 broadcaster_id: str 
 broadcaster_login: str 
 broadcaster_name: str 
 id: str 
 title: str 
 prompt: str 
 cost: int 
 image: object 
 url_1x: str 
 url_2x: str 
 url_4x: str 
 default_image: object 
 url_1x: str 
 url_2x: str 
 url_4x: str 
 background_color: str 
 is_enabled: bool 
 is_user_input_required: bool 
 max_per_stream_setting: object 
 is_enabled: bool 
 max_per_stream: None 
 max_per_user_per_stream_setting: object 
 is_enabled: bool 
 max_per_user_per_stream: None 
 global_cooldown_setting: object 
 is_enabled: bool 
 global_cooldown_seconds: None 
 is_paused: bool 
 is_in_stock: bool 
 should_redemptions_skip_request_queue: bool 
 redemptions_redeemed_current_stream: int 
 cooldown_expires_at: str 
 

Item_Index : 14
Get Custom Reward Redemption
data: list[object] 
 broadcaster_id: str 
 broadcaster_login: str 
 broadcaster_name: None 
 id: str 
 user_login: str 
 user_id: str 
 user_name: str 
 user_input: str 
 status: str 
 redeemed_at: str 
 reward: object 
 id: str 
 title: str 
 prompt: str 
 cost: None 
 

Item_Index : 16
Update Redemption Status
data: list[object] 
 broadcaster_id: str 
 broadcaster_login: str 
 broadcaster_name: str 
 id: str 
 user_id: str 
 user_name: str 
 user_login: str 
 reward: object 
 id: str 
 title: str 
 prompt: str 
 cost: None 
 user_input: str 
 status: str 
 redeemed_at: str 
 

Item_Index : 17
Get Charity Campaign
data: list[object] 
 id: str 
 broadcaster_id: str 
 broadcaster_login: str 
 broadcaster_name: str 
 charity_name: str 
 charity_description: str 
 charity_logo: str 
 charity_website: str 
 current_amount: object 
 value: int 
 decimal_places: int 
 currency: str 
 target_amount: object 
 value: int 
 decimal_places: int 
 currency: str 
 

Item_Index : 18
Get Charity Campaign Donations
data: list[object] 
 id: str 
 campaign_id: str 
 user_id: str 
 user_login: str 
 user_name: str 
 amount: object 
 value: int 
 decimal_places: int 
 currency: str 
 pagination: object 
 cursor: str 
 

Item_Index : 19
Get Chatters
data: list[object] 
 user_id: str 
 user_login: str 
 user_name: str 
 pagination: object 
 cursor: str 
 total: int 
 

Item_Index : 20
Get Channel Emotes
data: list[object] 
 id: str 
 name: str 
 images: object 
 url_1x: str 
 url_2x: str 
 url_4x: str 
 tier: str 
 emote_type: str 
 emote_set_id: str 
 format: list[str] 
 scale: list[str] 
 theme_mode: list[str] 
 template: str 
 

Item_Index : 21
Get Global Emotes
data: list[object] 
 id: str 
 name: str 
 images: object 
 url_1x: str 
 url_2x: str 
 url_4x: str 
 format: list[str] 
 scale: list[str] 
 theme_mode: list[str] 
 template: str 
 

Item_Index : 22
Get Emote Sets
data: list[object] 
 id: str 
 name: str 
 images: object 
 url_1x: str 
 url_2x: str 
 url_4x: str 
 emote_type: str 
 emote_set_id: str 
 owner_id: str 
 format: list[str] 
 scale: list[str] 
 theme_mode: list[str] 
 template: None 
 

Item_Index : 23
Get Channel Chat Badges
data: list[object] 
 set_id: str 
 versions: list[object] 
 id: str 
 image_url_1x: str 
 image_url_2x: str 
 image_url_4x: str 
 title: str 
 description: str 
 click_action: str 
 click_url: str 
 

Item_Index : 24
Get Global Chat Badges
data: list[object] 
 set_id: str 
 versions: list[object] 
 id: str 
 image_url_1x: str 
 image_url_2x: str 
 image_url_4x: str 
 title: str 
 description: str 
 click_action: str 
 click_url: str 
 

Item_Index : 25
Get Chat Settings
data: list[object] 
 broadcaster_id: str 
 emote_mode: bool 
 follower_mode: bool 
 follower_mode_duration: int 
 moderator_id: str 
 non_moderator_chat_delay: bool 
 non_moderator_chat_delay_duration: int 
 slow_mode: bool 
 slow_mode_wait_time: int 
 subscriber_mode: bool 
 unique_chat_mode: bool 
 

Item_Index : 26
Update Chat Settings
data: list[object] 
 broadcaster_id: str 
 emote_mode: bool 
 follower_mode: bool 
 follower_mode_duration: int 
 moderator_id: str 
 non_moderator_chat_delay: bool 
 non_moderator_chat_delay_duration: int 
 slow_mode: bool 
 slow_mode_wait_time: int 
 subscriber_mode: bool 
 unique_chat_mode: bool 
 message: str 
 color: str 
 

Item_Index : 29
Get User Chat Color
data: list[object] 
 user_id: str 
 user_login: str 
 user_name: str 
 color: str 
 edit_url: str 
 id: str 
 

Item_Index : 32
Get Clips
data: list[object] 
 id: str 
 url: str 
 embed_url: str 
 broadcaster_id: str 
 broadcaster_name: str 
 creator_id: str 
 creator_name: str 
 video_id: str 
 game_id: str 
 language: str 
 title: str 
 view_count: int 
 created_at: str 
 thumbnail_url: str 
 duration: None 
 vod_offset: int 
 pagination: object 
 cursor: str 
 

Item_Index : 33
Get Drops Entitlements
data: list[object] 
 id: str 
 benefit_id: str 
 timestamp: str 
 user_id: str 
 game_id: str 
 fulfillment_status: str 
 last_updated: str 
 pagination: object 
 cursor: str 
 

Item_Index : 34
Update Drops Entitlements
data: list[object] 
 status: str 
 ids: list[str] 
 

Item_Index : 35
Get Extension Configuration Segment
data: list[object] 
 segment: str 
 broadcaster_id: str 
 content: str 
 version: str 
 extension_id: str 
 segment: str 
 broadcaster_id: str 
 content: str 
 version: str 
 target: list[str] 
 broadcaster_id: None 
 is_global_broadcast: bool 
 message: str 
 

Item_Index : 39
Get Extension Live Channels
data: list[object] 
 broadcaster_id: str 
 broadcaster_name: str 
 game_name: str 
 game_id: str 
 title: str 
 pagination: str 
 

Item_Index : 40
Get Extension Secrets
data: list[object] 
 format_version: int 
 secrets: list[object] 
 content: str 
 active_at: str 
 expires_at: str 
 

Item_Index : 41
Create Extension Secret
data: list[object] 
 format_version: int 
 secrets: list[object] 
 content: str 
 active_at: str 
 expires_at: str 
 text: str 
 extension_id: str 
 extension_version: str 
 

Item_Index : 43
Get Extensions
data: list[object] 
 author_name: str 
 bits_enabled: bool 
 can_install: bool 
 configuration_location: str 
 description: str 
 eula_tos_url: str 
 has_chat_support: bool 
 icon_url: str 
 icon_urls: None 
 id: str 
 name: str 
 privacy_policy_url: str 
 request_identity_link: bool 
 screenshot_urls: list[str] 
 state: str 
 subscriptions_support_level: str 
 summary: str 
 support_email: str 
 version: str 
 viewer_summary: str 
 views: object 
 mobile: object 
 viewer_url: str 
 panel: object 
 viewer_url: str 
 height: int 
 can_link_external_content: bool 
 video_overlay: object 
 viewer_url: str 
 can_link_external_content: bool 
 component: object 
 viewer_url: str 
 aspect_ratio_x: int 
 aspect_ratio_y: int 
 autoscale: bool 
 scale_pixels: int 
 target_height: int 
 can_link_external_content: bool 
 config: object 
 viewer_url: str 
 can_link_external_content: bool 
 allowlisted_config_urls: list[str] 
 allowlisted_panel_urls: list[str] 
 

Item_Index : 44
Get Released Extensions
data: list[object] 
 author_name: str 
 bits_enabled: bool 
 can_install: bool 
 configuration_location: str 
 description: str 
 eula_tos_url: str 
 has_chat_support: bool 
 icon_url: str 
 icon_urls: None 
 id: str 
 name: str 
 privacy_policy_url: str 
 request_identity_link: bool 
 screenshot_urls: list[str] 
 state: str 
 subscriptions_support_level: str 
 summary: str 
 support_email: str 
 version: str 
 viewer_summary: str 
 views: object 
 mobile: object 
 viewer_url: str 
 panel: object 
 viewer_url: str 
 height: int 
 can_link_external_content: bool 
 video_overlay: object 
 viewer_url: str 
 can_link_external_content: bool 
 component: object 
 viewer_url: str 
 aspect_ratio_x: int 
 aspect_ratio_y: int 
 autoscale: bool 
 scale_pixels: int 
 target_height: int 
 can_link_external_content: bool 
 config: object 
 viewer_url: str 
 can_link_external_content: bool 
 allowlisted_config_urls: list[str] 
 allowlisted_panel_urls: list[str] 
 

Item_Index : 45
Get Extension Bits Products
data: list[object] 
 sku: str 
 cost: object 
 amount: int 
 type: str 
 in_development: bool 
 display_name: str 
 expiration: str 
 is_broadcast: bool 
 

Item_Index : 46
Update Extension Bits Product
data: list[object] 
 sku: str 
 cost: object 
 amount: int 
 type: str 
 in_development: bool 
 display_name: str 
 expiration: str 
 is_broadcast: bool 
 

Item_Index : 47
Create EventSub Subscription
data: list[object] 
 id: str 
 status: str 
 type: str 
 version: str 
 condition: object 
 created_at: str 
 transport: object 
 method: str 
 callback: str 
 session_id: str 
 connected_at: str 
 cost: int 
 total: int 
 total_cost: int 
 max_total_cost: int 
 

Item_Index : 49
Get EventSub Subscriptions
data: list[object] 
 id: str 
 status: str 
 type: str 
 version: str 
 condition: object 
 created_at: str 
 transport: object 
 method: str 
 callback: str 
 session_id: str 
 connected_at: str 
 disconnected_at: str 
 cost: int 
 total: int 
 total_cost: int 
 max_total_cost: int 
 pagination: object 
 cursor: str 
 

Item_Index : 52
Get Creator Goals
data: list[object] 
 id: str 
 broadcaster_id: str 
 broadcaster_name: str 
 broadcaster_login: str 
 type: str 
 description: str 
 current_amount: int 
 target_amount: int 
 created_at: None 
 

Item_Index : 53
Get Hype Train Events
data: list[object] 
 id: str 
 event_type: str 
 event_timestamp: str 
 version: str 
 event_data: object 
 broadcaster_id: str 
 cooldown_end_time: None 
 expires_at: str 
 goal: int 
 id: str 
 last_contribution: object 
 total: int 
 type: str 
 user: str 
 level: int 
 started_at: str 
 top_contributions: list[object] 
 total: int 
 type: str 
 user: str 
 total: int 
 pagination: object 
 cursor: str 
 

Item_Index : 54
Check AutoMod Status
data: list[object] 
 msg_id: str 
 is_permitted: bool 
 user_id: str 
 msg_id: str 
 action: str 
 

Item_Index : 56
Get AutoMod Settings
data: list[object] 
 broadcaster_id: str 
 moderator_id: str 
 overall_level: int 
 disability: int 
 aggression: int 
 sexuality_sex_or_gender: int 
 misogyny: int 
 bullying: int 
 swearing: int 
 race_ethnicity_or_religion: int 
 sex_based_terms: int 
 

Item_Index : 57
Update AutoMod Settings
data: list[object] 
 broadcaster_id: str 
 moderator_id: str 
 overall_level: int 
 disability: int 
 aggression: int 
 sexuality_sex_or_gender: int 
 misogyny: int 
 bullying: int 
 swearing: int 
 race_ethnicity_or_religion: int 
 sex_based_terms: int 
 

Item_Index : 58
Get Banned Users
data: list[object] 
 user_id: str 
 user_login: str 
 user_name: str 
 expires_at: str 
 created_at: str 
 reason: str 
 moderator_id: str 
 moderator_login: str 
 moderator_name: str 
 pagination: object 
 cursor: str 
 

Item_Index : 59
Ban User
data: list[object] 
 broadcaster_id: str 
 moderator_id: str 
 user_id: str 
 created_at: None 
 end_time: str 
 

Item_Index : 61
Get Blocked Terms
data: list[object] 
 broadcaster_id: str 
 moderator_id: str 
 id: str 
 text: str 
 created_at: str 
 updated_at: str 
 expires_at: str 
 pagination: object 
 cursor: str 
 

Item_Index : 62
Add Blocked Term
data: list[object] 
 broadcaster_id: str 
 moderator_id: str 
 id: str 
 text: str 
 created_at: str 
 updated_at: str 
 expires_at: str 
 

Item_Index : 65
Get Moderators
data: list[object] 
 user_id: str 
 user_login: str 
 user_name: str 
 pagination: object 
 cursor: str 
 

Item_Index : 68
Get VIPs
data: list[object] 
 user_id: str 
 user_name: str 
 user_login: str 
 pagination: object 
 cursor: str 
 

Item_Index : 71
Update Shield Mode Status
data: list[object] 
 is_active: bool 
 moderator_id: str 
 moderator_login: str 
 moderator_name: str 
 last_activated_at: str 
 

Item_Index : 72
Get Shield Mode Status
data: list[object] 
 is_active: bool 
 moderator_id: str 
 moderator_login: str 
 moderator_name: str 
 last_activated_at: str 
 

Item_Index : 73
Get Polls
data: list[object] 
 id: str 
 broadcaster_id: str 
 broadcaster_name: str 
 broadcaster_login: str 
 title: str 
 choices: list[object] 
 id: str 
 title: str 
 votes: int 
 channel_points_votes: int 
 bits_votes: int 
 bits_voting_enabled: bool 
 bits_per_vote: int 
 channel_points_voting_enabled: bool 
 channel_points_per_vote: int 
 status: str 
 duration: int 
 started_at: str 
 ended_at: str 
 pagination: object 
 cursor: str 
 

Item_Index : 74
Create Poll
data: list[object] 
 id: str 
 broadcaster_id: str 
 broadcaster_name: str 
 broadcaster_login: str 
 title: str 
 choices: list[object] 
 id: str 
 title: str 
 votes: int 
 channel_points_votes: int 
 bits_votes: int 
 bits_voting_enabled: bool 
 bits_per_vote: int 
 channel_points_voting_enabled: bool 
 channel_points_per_vote: int 
 status: str 
 duration: int 
 started_at: str 
 ended_at: str 
 

Item_Index : 75
End Poll
data: list[object] 
 id: str 
 broadcaster_id: str 
 broadcaster_name: str 
 broadcaster_login: str 
 title: str 
 choices: list[object] 
 id: str 
 title: str 
 votes: int 
 channel_points_votes: int 
 bits_votes: int 
 bits_voting_enabled: bool 
 bits_per_vote: int 
 channel_points_voting_enabled: bool 
 channel_points_per_vote: int 
 status: str 
 duration: int 
 started_at: str 
 ended_at: str 
 

Item_Index : 76
Get Predictions
data: list[object] 
 id: str 
 broadcaster_id: str 
 broadcaster_name: str 
 broadcaster_login: str 
 title: str 
 winning_outcome_id: str 
 outcomes: list[object] 
 id: str 
 title: str 
 users: int 
 channel_points: int 
 top_predictors: list[object] 
 user_id: str 
 user_name: str 
 user_login: str 
 channel_points_used: int 
 channel_points_won: int 
 color: str 
 prediction_window: int 
 status: str 
 created_at: str 
 ended_at: str 
 locked_at: str 
 pagination: object 
 cursor: str 
 

Item_Index : 77
Create Prediction
data: list[object] 
 id: str 
 broadcaster_id: str 
 broadcaster_name: str 
 broadcaster_login: str 
 title: str 
 winning_outcome_id: str 
 outcomes: list[object] 
 id: str 
 title: str 
 users: int 
 channel_points: int 
 top_predictors: list[object] 
 user_id: str 
 user_name: str 
 user_login: str 
 channel_points_used: int 
 channel_points_won: int 
 color: str 
 prediction_window: int 
 status: str 
 created_at: str 
 ended_at: str 
 locked_at: str 
 

Item_Index : 78
End Prediction
data: list[object] 
 id: str 
 broadcaster_id: str 
 broadcaster_name: str 
 broadcaster_login: str 
 title: str 
 winning_outcome_id: str 
 outcomes: list[object] 
 id: str 
 title: str 
 users: int 
 channel_points: int 
 top_predictors: list[object] 
 user_id: str 
 user_name: str 
 user_login: str 
 channel_points_used: int 
 channel_points_won: int 
 color: str 
 prediction_window: int 
 status: str 
 created_at: str 
 ended_at: str 
 locked_at: str 
 

Item_Index : 79
Start a raid
data: list[object] 
 created_at: str 
 is_mature: bool 
 

Item_Index : 81
Get Channel Stream Schedule
data: object 
 segments: list[object] 
 id: str 
 start_time: str 
 end_time: str 
 title: str 
 canceled_until: str 
 category: object 
 id: str 
 name: str 
 is_recurring: bool 
 broadcaster_id: str 
 broadcaster_name: str 
 broadcaster_login: str 
 vacation: object 
 start_time: str 
 end_time: str 
 pagination: object 
 cursor: str 
 

Item_Index : 84
Create Channel Stream Schedule Segment
data: object 
 segments: list[object] 
 id: str 
 start_time: str 
 end_time: str 
 title: str 
 canceled_until: str 
 category: object 
 id: str 
 name: str 
 is_recurring: bool 
 broadcaster_id: str 
 broadcaster_name: str 
 broadcaster_login: str 
 vacation: object 
 start_time: str 
 end_time: str 
 

Item_Index : 85
Update Channel Stream Schedule Segment
data: object 
 segments: list[object] 
 id: str 
 start_time: str 
 end_time: str 
 title: str 
 canceled_until: str 
 category: object 
 id: str 
 name: str 
 is_recurring: bool 
 broadcaster_id: str 
 broadcaster_name: str 
 broadcaster_login: str 
 vacation: object 
 start_time: str 
 end_time: str 
 

Item_Index : 87
Search Categories
data: list[object] 
 box_art_url: str 
 name: str 
 id: str 
 

Item_Index : 88
Search Channels
data: list[object] 
 box_art_url: str 
 name: str 
 id: str 
 

Item_Index : 89
Get Soundtrack Current Track
data: list[object] 
 track: object 
 album: object 
 id: str 
 image_url: str 
 name: str 
 artists: list[object] 
 creator_channel_id: str 
 id: str 
 name: str 
 duration: int 
 id: str 
 isrc: str 
 title: str 
 source: object 
 content_type: str 
 id: str 
 image_url: str 
 soundtrack_url: str 
 spotify_url: str 
 title: str 
 

Item_Index : 90
Get Soundtrack Playlist
data: list[object] 
 album: object 
 id: str 
 image_url: str 
 name: str 
 artists: list[object] 
 creator_channel_id: str 
 id: str 
 name: str 
 duration: int 
 id: str 
 isrc: str 
 title: str 
 pagination: object 
 cursor: str 
 

Item_Index : 91
Get Soundtrack Playlists
data: list[object] 
 description: str 
 id: str 
 image_url: str 
 title: str 
 pagination: object 
 cursor: str 
 

Item_Index : 92
Get Stream Key
data: list[object] 
 stream_key: str 
 

Item_Index : 93
Get Streams
data: list[object] 
 id: str 
 user_id: str 
 user_login: str 
 user_name: str 
 game_id: str 
 game_name: str 
 type: str 
 title: str 
 tags: list[str] 
 viewer_count: int 
 started_at: str 
 language: str 
 thumbnail_url: str 
 tag_ids: list[str] 
 is_mature: bool 
 pagination: object 
 cursor: str 
 

Item_Index : 94
Get Followed Streams
data: list[object] 
 id: str 
 user_id: str 
 user_login: str 
 user_name: str 
 game_id: str 
 game_name: str 
 type: str 
 title: str 
 viewer_count: int 
 started_at: str 
 language: str 
 thumbnail_url: str 
 tag_ids: list[str] 
 tags: list[str] 
 is_mature: bool 
 pagination: object 
 cursor: str 
 

Item_Index : 95
Create Stream Marker
data: list[object] 
 id: str 
 created_at: str 
 position_seconds: int 
 description: str 
 

Item_Index : 96
Get Stream Markers
data: list[object] 
 user_id: str 
 user_name: str 
 user_login: str 
 videos: list[object] 
 video_id: str 
 markers: list[object] 
 id: str 
 created_at: str 
 description: str 
 position_seconds: int 
 url: str 
 pagination: object 
 cursor: str 
 

Item_Index : 97
Get Broadcaster Subscriptions
data: list[object] 
 broadcaster_id: str 
 broadcaster_login: str 
 broadcaster_name: str 
 gifter_id: str 
 gifter_login: str 
 gifter_name: str 
 is_gift: bool 
 plan_name: str 
 tier: str 
 user_id: str 
 user_name: str 
 user_login: str 
 pagination: object 
 cursor: str 
 points: int 
 total: int 
 

Item_Index : 98
Check User Subscription
data: list[object] 
 broadcaster_id: str 
 broadcaster_login: str 
 broadcaster_name: str 
 gifter_id: str 
 gifter_login: str 
 gifter_name: str 
 is_gift: bool 
 tier: str 
 

Item_Index : 99
Get All Stream Tags
data: list[object] 
 tag_id: str 
 is_auto: bool 
 localization_names: None 
 localization_descriptions: None 
 pagination: object 
 cursor: str 
 

Item_Index : 100
Get Stream Tags
data: list[object] 
 tag_id: str 
 is_auto: bool 
 localization_names: None 
 localization_descriptions: None 
 

Item_Index : 101
Get Channel Teams
data: list[object] 
 broadcaster_id: str 
 broadcaster_login: str 
 broadcaster_name: str 
 background_image_url: str 
 banner: str 
 created_at: str 
 updated_at: str 
 info: str 
 thumbnail_url: str 
 team_name: str 
 team_display_name: str 
 id: str 
 

Item_Index : 102
Get Teams
data: list[object] 
 users: list[object] 
 user_id: str 
 user_login: str 
 user_name: str 
 background_image_url: str 
 banner: str 
 created_at: str 
 updated_at: str 
 info: str 
 thumbnail_url: str 
 team_name: str 
 team_display_name: str 
 id: str 
 

Item_Index : 103
Get Users
data: list[object] 
 id: str 
 login: str 
 display_name: str 
 type: str 
 broadcaster_type: str 
 description: str 
 profile_image_url: str 
 offline_image_url: str 
 view_count: int 
 email: str 
 created_at: str 
 

Item_Index : 104
Update User
data: list[object] 
 id: str 
 login: str 
 display_name: str 
 type: str 
 broadcaster_type: str 
 description: str 
 profile_image_url: str 
 offline_image_url: str 
 view_count: int 
 email: str 
 created_at: str 
 total: int 
 

Item_Index : 105
Get Users Follows
data: list[object] 
 from_id: str 
 from_login: str 
 from_name: str 
 to_id: str 
 to_login: str 
 to_name: str 
 followed_at: str 
 pagination: object 
 cursor: str 
 

Item_Index : 106
Get User Block List
data: list[object] 
 user_id: str 
 user_login: str 
 display_name: str 
 

Item_Index : 109
Get User Extensions
data: list[object] 
 id: str 
 version: str 
 name: str 
 can_activate: bool 
 type: list[str] 
 

Item_Index : 110
Get User Active Extensions
data: object 
 panel: None 
 active: bool 
 id: str 
 version: str 
 name: str 
 overlay: None 
 active: bool 
 id: str 
 version: str 
 name: str 
 component: None 
 active: bool 
 id: str 
 version: str 
 name: str 
 x: int 
 y: int 
 

Item_Index : 111
Update User Extensions
data: object 
 panel: None 
 active: bool 
 id: str 
 version: str 
 name: str 
 overlay: None 
 active: bool 
 id: str 
 version: str 
 name: str 
 component: None 
 active: bool 
 id: str 
 version: str 
 name: str 
 x: int 
 y: int 
 message: str 
 