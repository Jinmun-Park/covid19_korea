import pandas as pd
import datetime as dt
from src.utils.api import flask_category

# ====================== Flask Blueprint ====================== #
from flask import Blueprint, render_template
df, df_category, df_channeltitle, df_category_view_per, df_category_like_per, df_category_comment_per, df_top_channel, df_top_category, df_top_comment = flask_category(command='daily')
bp = Blueprint('latest_trend', __name__, url_prefix='/latest_trend')

# ======================== Flask Route ======================== #
@bp.route('/', methods=["GET"])
def trend():
    # Chart figures
    category = [i for i in df_category.index]
    category_rate = [i for i in df_category.카테고리]
    category_view_per = [i for i in df_category_view_per.조회수]
    category_like_per = [i for i in df_category_like_per.좋아요수]
    category_comment_per = [i for i in df_category_comment_per.댓글수]
    # Table
    category_channel = df.groupby(['카테고리', '채널명']).sum().sort_values('조회수', ascending=False).reset_index()
    category_channel['조회수'] = category_channel['조회수'].map("{:,}".format)
    category_channel['좋아요수'] = category_channel['좋아요수'].map("{:,}".format)
    category_channel['댓글수'] = category_channel['댓글수'].map("{:,}".format)
    # Chart Basic information figures
    category_top_channel = df_top_channel.채널명.iloc[0]
    category_top_category = df_top_category.카테고리.iloc[0]
    category_top_comment = format(df_top_comment.댓글수.iloc[0], ",")
    return render_template('latest_trend.html',
                           category=category,
                           category_rate=category_rate,
                           category_channel=category_channel,
                           category_view_per=category_view_per,
                           category_like_per=category_like_per,
                           category_comment_per=category_comment_per,
                           category_top_channel=category_top_channel,
                           category_top_category=category_top_category,
                           category_top_comment=category_top_comment
                           )

@bp.route('/category', methods=["GET"])
def trend_category():
    # Chart figures
    category = [i for i in df_category.index]
    category_rate = [i for i in df_category.카테고리]
    category_view_per = [i for i in df_category_view_per.조회수]
    category_like_per = [i for i in df_category_like_per.좋아요수]
    category_comment_per = [i for i in df_category_comment_per.댓글수]
    # Table
    category_channel = df.groupby(['카테고리', '채널명']).sum().sort_values('조회수', ascending=False).reset_index()
    category_channel['조회수'] = category_channel['조회수'].map("{:,}".format)
    category_channel['좋아요수'] = category_channel['좋아요수'].map("{:,}".format)
    category_channel['댓글수'] = category_channel['댓글수'].map("{:,}".format)
    # Chart basic information figures
    category_top_channel = df_top_channel.채널명.iloc[0]
    category_top_category = df_top_category.카테고리.iloc[0]
    category_top_comment = format(df_top_comment.댓글수.iloc[0], ",")
    return render_template('category.html',
                           category=category,
                           category_rate=category_rate,
                           category_channel=category_channel,
                           category_view_per=category_view_per,
                           category_like_per=category_like_per,
                           category_comment_per=category_comment_per,
                           category_top_channel=category_top_channel,
                           category_top_category=category_top_category,
                           category_top_comment=category_top_comment
                           )

@bp.route('/channel', methods=["GET"])
def trend_channel():
    # Importing function
    if 'flask_channel' in globals():
        pass
    else:
        from src.utils.api import flask_channel
        global flask_channel
        flask_channel = flask_channel(command='daily')
    # Channel names
    channel_label = [i for i in flask_channel.채널명]
    channel_view = [i for i in (flask_channel.채널총조회수)/1000]
    channel_subs = [i for i in (flask_channel.채널구독수)]
    # Top channel information figures
    top_channel_select = flask_channel[flask_channel['채널총조회수'] == flask_channel['채널총조회수'].max()]
    top_channel = top_channel_select.채널명.iloc[0]
    top_channel_num = format(int(top_channel_select.채널총조회수.iloc[0]), ",")
    # Top channel top right information
    top_channel_url = top_channel_select.썸네일.iloc[0]
    top_channel_videoid = top_channel_select.동영상아이디.iloc[0]
    top_channel_channelid = top_channel_select.채널아이디.iloc[0]
    top_channel_publish = top_channel_select.채널개설날짜.iloc[0]
    top_channel_cateogry = top_channel_select.카테고리.iloc[0]
    top_channel_like = format(int(top_channel_select.좋아요수.iloc[0]), ",")
    top_channel_comment = format(int(top_channel_select.댓글수.iloc[0]), ",")
    # Top channel subscriptions
    top_subs_num = format(int(flask_channel[flask_channel['채널구독수'] == flask_channel['채널구독수'].max()].채널구독수.iloc[0]), ",")
    top_subs = flask_channel[flask_channel['채널구독수'] == flask_channel['채널구독수'].max()].채널명.iloc[0]
    # Latest published channel
    latest_channel_select = flask_channel.sort_values(by='채널개설날짜').tail(1)
    latest_channel = latest_channel_select.채널명.iloc[0]
    latest_channel_num = latest_channel_select.채널개설날짜.iloc[0]
    # Top channel top right information
    latest_channel_url = latest_channel_select.썸네일.iloc[0]
    latest_channel_videoid = latest_channel_select.동영상아이디.iloc[0]
    latest_channel_channelid = latest_channel_select.채널아이디.iloc[0]
    #latest_channel_publish = latest_channel_select.채널개설날짜.iloc[0]
    latest_channel_cateogry = latest_channel_select.카테고리.iloc[0]
    latest_channel_like = format(int(latest_channel_select.좋아요수.iloc[0]), ",")
    latest_channel_comment = format(int(latest_channel_select.댓글수.iloc[0]), ",")
    # trend_channel_chart
    channel_table = flask_channel[['동영상', '날짜', '채널명',  '채널개설날짜', '카테고리',  '채널총조회수', '채널구독수', '채널비디오수']]
    return render_template('channel.html',
                           channel_label=channel_label,
                           channel_view=channel_view,
                           channel_subs=channel_subs,
                           top_channel=top_channel,
                           top_channel_num=top_channel_num,
                           top_channel_url=top_channel_url,
                           top_channel_videoid=top_channel_videoid,
                           top_channel_channelid=top_channel_channelid,
                           top_channel_publish= top_channel_publish,
                           top_channel_cateogry=top_channel_cateogry,
                           top_channel_like=top_channel_like,
                           top_channel_comment=top_channel_comment,
                           top_subs=top_subs,
                           top_subs_num=top_subs_num,
                           latest_channel=latest_channel,
                           latest_channel_num=latest_channel_num,
                           latest_channel_url=latest_channel_url,
                           latest_channel_videoid=latest_channel_videoid,
                           latest_channel_channelid=latest_channel_channelid,
                           latest_channel_cateogry=latest_channel_cateogry,
                           latest_channel_like=latest_channel_like,
                           latest_channel_comment=latest_channel_comment,
                           channel_table=channel_table
                           )

@bp.route('/timeframe', methods=["GET"])
def trend_timeframe():
    db = flask_channel
    return render_template('timeframe.html', db=db)
