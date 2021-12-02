from src.models.bert_load import run_predict
from flask import Blueprint, render_template, request, redirect
from src.utils.api import channel_search
from src.utils.api import pickle_videos, pickle_videos_filter, pickle_videos_comments
from src.utils.api import globals_videos, globals_videos_filter, globals_videos_comments
import pandas as pd
import pickle

bp = Blueprint('dashboard', __name__, url_prefix='/dashboard')

@bp.route('/', methods=["GET"])
def search():
    return render_template('dashboard.html')

@bp.route('/channel_result', methods=["GET"])
def search_result():
    chanel_name = request.args.get('cha_name')
    search = channel_search(chanel_name)
    return render_template('channel_result.html', title=chanel_name, data=search, titles=['channel_id', 'published_at', 'channel_title', 'view_count','subscriber_count', 'video_count'])

@bp.route('/video_result', methods=['GET', 'POST'])
def video_result():
    if request.method == "POST":
        channel_id = request.form.get("channel_id")
        vid = pickle_videos(type='sample', channel_id=channel_id)
        # vid = globals_videos(type='sample', channel_id=channel_id)
        # vid = pd.read_pickle('Pickle/video_sample_info.pkl')
        return render_template('video_result.html', title=channel_id, vid=vid, titles=['video_id', 'video_title', 'published_at', 'view_count', 'like_count', 'comment_count', 'wiki_category'])

@bp.route('/filter_result', methods=["GET"])
def video_filter():
    find = request.args.get('find')
    vid_filter = pickle_videos_filter(type='sample', find=find)
    # vid_filter = globals_videos_filter(find)
    # vid_filter = pd.read_pickle('Pickle/video_info_filter.pkl')
    return render_template('keyword_result.html', title=find, vid=vid_filter, titles=['video_id', 'video_title', 'published_at', 'view_count', 'like_count', 'comment_count', 'wiki_category'])

@bp.route('/comment_result', methods=["GET"])
def video_comment():
    vid_comments = pickle_videos_comments(type='sample', option='save')
    # data = pd.read_pickle('Pickle/video_comment.pkl')
    return render_template('comment_result.html', data=vid_comments, titles=['comment_id', 'comment', 'author', 'like_count', 'published_at','reply_count'])







