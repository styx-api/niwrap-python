# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

V__MAKE_LABEL_TABLE_METADATA = Metadata(
    id="287075a9705f1e3aa4609a67bab5671fa4e1d6b9.boutiques",
    name="@MakeLabelTable",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


VMakeLabelTableParameters = typing.TypedDict('VMakeLabelTableParameters', {
    "__STYX_TYPE__": typing.Literal["@MakeLabelTable"],
    "labeltable": str,
    "atlas_pointlist": typing.NotRequired[str | None],
    "lab_r": typing.NotRequired[list[str] | None],
    "lab_v": typing.NotRequired[list[str] | None],
    "lab_file_delim": typing.NotRequired[str | None],
    "lab_file": typing.NotRequired[list[str] | None],
    "dset": typing.NotRequired[InputPathType | None],
    "longnames": typing.NotRequired[float | None],
    "last_longname_col": typing.NotRequired[float | None],
    "centers": bool,
    "centertype": typing.NotRequired[str | None],
    "centermask": typing.NotRequired[str | None],
    "skip_novoxels": bool,
    "all_labels": bool,
    "all_keys": bool,
    "lkeys": typing.NotRequired[str | None],
    "rkeys": typing.NotRequired[str | None],
    "klabel": typing.NotRequired[str | None],
    "match_label": typing.NotRequired[str | None],
    "labeltable_of_dset": typing.NotRequired[InputPathType | None],
    "word_label_match": bool,
    "quiet_death": bool,
    "lt_to_atlas_pl": typing.NotRequired[str | None],
    "dset_lt_to_atlas_pl": typing.NotRequired[list[InputPathType] | None],
    "lt_to_csv": typing.NotRequired[InputPathType | None],
    "atlasize_labeled_dset": typing.NotRequired[InputPathType | None],
    "atlas_file": typing.NotRequired[str | None],
    "atlas_name": typing.NotRequired[str | None],
    "atlas_description": typing.NotRequired[str | None],
    "replace": bool,
    "add_atlas_dset": typing.NotRequired[InputPathType | None],
    "h_web": bool,
    "h_view": bool,
    "all_opts": bool,
    "h_find": typing.NotRequired[str | None],
})


def dyn_cargs(
    t: str,
) -> typing.Any:
    """
    Get build cargs function by command type.
    
    Args:
        t: Command type.
    Returns:
        Build cargs function.
    """
    return {
        "@MakeLabelTable": v__make_label_table_cargs,
    }.get(t)


def dyn_outputs(
    t: str,
) -> typing.Any:
    """
    Get build outputs function by command type.
    
    Args:
        t: Command type.
    Returns:
        Build outputs function.
    """
    return {
        "@MakeLabelTable": v__make_label_table_outputs,
    }.get(t)


class VMakeLabelTableOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v__make_label_table(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_labeltable: OutputPathType
    """Output label table file"""
    output_atlas_pointlist: OutputPathType | None
    """Output atlas point list file"""
    output_csv: OutputPathType | None
    """Output CSV file from label table"""
    output_niml_atlas: OutputPathType | None
    """Output NIML file after atlasizing labeled dataset"""


def v__make_label_table_params(
    labeltable: str,
    atlas_pointlist: str | None = None,
    lab_r: list[str] | None = None,
    lab_v: list[str] | None = None,
    lab_file_delim: str | None = None,
    lab_file: list[str] | None = None,
    dset: InputPathType | None = None,
    longnames: float | None = None,
    last_longname_col: float | None = None,
    centers: bool = False,
    centertype: str | None = None,
    centermask: str | None = None,
    skip_novoxels: bool = False,
    all_labels: bool = False,
    all_keys: bool = False,
    lkeys: str | None = None,
    rkeys: str | None = None,
    klabel: str | None = None,
    match_label: str | None = None,
    labeltable_of_dset: InputPathType | None = None,
    word_label_match: bool = False,
    quiet_death: bool = False,
    lt_to_atlas_pl: str | None = None,
    dset_lt_to_atlas_pl: list[InputPathType] | None = None,
    lt_to_csv: InputPathType | None = None,
    atlasize_labeled_dset: InputPathType | None = None,
    atlas_file: str | None = None,
    atlas_name: str | None = None,
    atlas_description: str | None = None,
    replace: bool = False,
    add_atlas_dset: InputPathType | None = None,
    h_web: bool = False,
    h_view: bool = False,
    all_opts: bool = False,
    h_find: str | None = None,
) -> VMakeLabelTableParameters:
    """
    Build parameters.
    
    Args:
        labeltable: Name of output label table.
        atlas_pointlist: Instead of a label table, produce an atlas point list.
        lab_r: Define a label with its minimum and maximum key values.
        lab_v: Define a label and its value.
        lab_file_delim: Set column delimiter for -lab_file option.
        lab_file: Specify labels and keys from a text file.
        dset: Attach the label table (or atlas point list) to dataset.
        longnames: Allow for another column of long names for regions.
        last_longname_col: Limit long names to nth column.
        centers: Compute center of mass location for each ROI.
        centertype: Different ways to compute centers (Icent, Dcent, cm).
        centermask: Calculate center of mass locations using a subset of voxels.
        skip_novoxels: Skip regions without voxels.
        all_labels: Return a listing of all labels.
        all_keys: Return a listing of all keys.
        lkeys: Return the keys whose labels match a given label.
        rkeys: Return the range (min max) of keys whose labels match a given\
            label.
        klabel: Return the label associated with a given key.
        match_label: Return labels matching a given label.
        labeltable_of_dset: Dump the labeltable from a dataset.
        word_label_match: Use word matching for labels.
        quiet_death: Do not give error messages when failing.
        lt_to_atlas_pl: Transform Label Table to Atlas Point List.
        dset_lt_to_atlas_pl: Get Label Table in dataset and write as an Atlas\
            Point List.
        lt_to_csv: Transform Label Table to CSV format.
        atlasize_labeled_dset: Transform a labeled ROI dataset into an atlas.
        atlas_file: Specify the name of the NIML file where atlas attributes\
            are stored.
        atlas_name: Name of the Atlas.
        atlas_description: Description of the Atlas, which appears in AFNI's\
            whereami window.
        replace: Replace existing Atlas if the name already exists in the NIML\
            file.
        add_atlas_dset: Add an existing atlas to an atlas file.
        h_web: Open webpage with help for this program.
        h_view: Open -help output in a GUI editor.
        all_opts: List all of the options for this script.
        h_find: Search for lines containing a specific word in the help output.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "@MakeLabelTable",
        "labeltable": labeltable,
        "centers": centers,
        "skip_novoxels": skip_novoxels,
        "all_labels": all_labels,
        "all_keys": all_keys,
        "word_label_match": word_label_match,
        "quiet_death": quiet_death,
        "replace": replace,
        "h_web": h_web,
        "h_view": h_view,
        "all_opts": all_opts,
    }
    if atlas_pointlist is not None:
        params["atlas_pointlist"] = atlas_pointlist
    if lab_r is not None:
        params["lab_r"] = lab_r
    if lab_v is not None:
        params["lab_v"] = lab_v
    if lab_file_delim is not None:
        params["lab_file_delim"] = lab_file_delim
    if lab_file is not None:
        params["lab_file"] = lab_file
    if dset is not None:
        params["dset"] = dset
    if longnames is not None:
        params["longnames"] = longnames
    if last_longname_col is not None:
        params["last_longname_col"] = last_longname_col
    if centertype is not None:
        params["centertype"] = centertype
    if centermask is not None:
        params["centermask"] = centermask
    if lkeys is not None:
        params["lkeys"] = lkeys
    if rkeys is not None:
        params["rkeys"] = rkeys
    if klabel is not None:
        params["klabel"] = klabel
    if match_label is not None:
        params["match_label"] = match_label
    if labeltable_of_dset is not None:
        params["labeltable_of_dset"] = labeltable_of_dset
    if lt_to_atlas_pl is not None:
        params["lt_to_atlas_pl"] = lt_to_atlas_pl
    if dset_lt_to_atlas_pl is not None:
        params["dset_lt_to_atlas_pl"] = dset_lt_to_atlas_pl
    if lt_to_csv is not None:
        params["lt_to_csv"] = lt_to_csv
    if atlasize_labeled_dset is not None:
        params["atlasize_labeled_dset"] = atlasize_labeled_dset
    if atlas_file is not None:
        params["atlas_file"] = atlas_file
    if atlas_name is not None:
        params["atlas_name"] = atlas_name
    if atlas_description is not None:
        params["atlas_description"] = atlas_description
    if add_atlas_dset is not None:
        params["add_atlas_dset"] = add_atlas_dset
    if h_find is not None:
        params["h_find"] = h_find
    return params


def v__make_label_table_cargs(
    params: VMakeLabelTableParameters,
    execution: Execution,
) -> list[str]:
    """
    Build command-line arguments from parameters.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Command-line arguments.
    """
    cargs = []
    cargs.append("@MakeLabelTable")
    cargs.extend([
        "-labeltable",
        params.get("labeltable")
    ])
    if params.get("atlas_pointlist") is not None:
        cargs.extend([
            "-atlas_pointlist",
            params.get("atlas_pointlist")
        ])
    if params.get("lab_r") is not None:
        cargs.extend([
            "-lab_r",
            *params.get("lab_r")
        ])
    if params.get("lab_v") is not None:
        cargs.extend([
            "-lab_v",
            *params.get("lab_v")
        ])
    if params.get("lab_file_delim") is not None:
        cargs.extend([
            "-lab_file_delim",
            params.get("lab_file_delim")
        ])
    if params.get("lab_file") is not None:
        cargs.extend([
            "-lab_file",
            *params.get("lab_file")
        ])
    if params.get("dset") is not None:
        cargs.extend([
            "-dset",
            execution.input_file(params.get("dset"))
        ])
    if params.get("longnames") is not None:
        cargs.extend([
            "-longnames",
            str(params.get("longnames"))
        ])
    if params.get("last_longname_col") is not None:
        cargs.extend([
            "-last_longname_col",
            str(params.get("last_longname_col"))
        ])
    if params.get("centers"):
        cargs.append("-centers")
    if params.get("centertype") is not None:
        cargs.extend([
            "-centertype",
            params.get("centertype")
        ])
    if params.get("centermask") is not None:
        cargs.extend([
            "-centermask",
            params.get("centermask")
        ])
    if params.get("skip_novoxels"):
        cargs.append("-skip_novoxels")
    if params.get("all_labels"):
        cargs.append("-all_labels")
    if params.get("all_keys"):
        cargs.append("-all_keys")
    if params.get("lkeys") is not None:
        cargs.extend([
            "-lkeys",
            params.get("lkeys")
        ])
    if params.get("rkeys") is not None:
        cargs.extend([
            "-rkeys",
            params.get("rkeys")
        ])
    if params.get("klabel") is not None:
        cargs.extend([
            "-klabel",
            params.get("klabel")
        ])
    if params.get("match_label") is not None:
        cargs.extend([
            "-match_label",
            params.get("match_label")
        ])
    if params.get("labeltable_of_dset") is not None:
        cargs.extend([
            "-labeltable_of_dset",
            execution.input_file(params.get("labeltable_of_dset"))
        ])
    if params.get("word_label_match"):
        cargs.append("-word_label_match")
    if params.get("quiet_death"):
        cargs.append("-quiet_death")
    if params.get("lt_to_atlas_pl") is not None:
        cargs.extend([
            "-LT_to_atlas_PL",
            params.get("lt_to_atlas_pl")
        ])
    if params.get("dset_lt_to_atlas_pl") is not None:
        cargs.extend([
            "-dset_LT_to_atlas_PL",
            *[execution.input_file(f) for f in params.get("dset_lt_to_atlas_pl")]
        ])
    if params.get("lt_to_csv") is not None:
        cargs.extend([
            "-LT_to_CSV",
            execution.input_file(params.get("lt_to_csv"))
        ])
    if params.get("atlasize_labeled_dset") is not None:
        cargs.extend([
            "-atlasize_labeled_dset",
            execution.input_file(params.get("atlasize_labeled_dset"))
        ])
    if params.get("atlas_file") is not None:
        cargs.extend([
            "-atlas_file",
            params.get("atlas_file")
        ])
    if params.get("atlas_name") is not None:
        cargs.extend([
            "-atlas_name",
            params.get("atlas_name")
        ])
    if params.get("atlas_description") is not None:
        cargs.extend([
            "-atlas_description",
            params.get("atlas_description")
        ])
    if params.get("replace"):
        cargs.append("-replace")
    if params.get("add_atlas_dset") is not None:
        cargs.extend([
            "-add_atlas_dset",
            execution.input_file(params.get("add_atlas_dset"))
        ])
    if params.get("h_web"):
        cargs.append("-h_web")
    if params.get("h_view"):
        cargs.append("-h_view")
    if params.get("all_opts"):
        cargs.append("-all_opts")
    if params.get("h_find") is not None:
        cargs.extend([
            "-h_find",
            params.get("h_find")
        ])
    return cargs


def v__make_label_table_outputs(
    params: VMakeLabelTableParameters,
    execution: Execution,
) -> VMakeLabelTableOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = VMakeLabelTableOutputs(
        root=execution.output_file("."),
        output_labeltable=execution.output_file(params.get("labeltable") + ".niml.lt"),
        output_atlas_pointlist=execution.output_file(params.get("atlas_pointlist") + ".niml.atlas") if (params.get("atlas_pointlist") is not None) else None,
        output_csv=execution.output_file(pathlib.Path(params.get("lt_to_csv")).name + ".csv") if (params.get("lt_to_csv") is not None) else None,
        output_niml_atlas=execution.output_file(pathlib.Path(params.get("atlasize_labeled_dset")).name + ".niml") if (params.get("atlasize_labeled_dset") is not None) else None,
    )
    return ret


def v__make_label_table_execute(
    params: VMakeLabelTableParameters,
    execution: Execution,
) -> VMakeLabelTableOutputs:
    """
    Script used to create, modify, and transform label tables.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `VMakeLabelTableOutputs`).
    """
    params = execution.params(params)
    cargs = v__make_label_table_cargs(params, execution)
    ret = v__make_label_table_outputs(params, execution)
    execution.run(cargs)
    return ret


def v__make_label_table(
    labeltable: str,
    atlas_pointlist: str | None = None,
    lab_r: list[str] | None = None,
    lab_v: list[str] | None = None,
    lab_file_delim: str | None = None,
    lab_file: list[str] | None = None,
    dset: InputPathType | None = None,
    longnames: float | None = None,
    last_longname_col: float | None = None,
    centers: bool = False,
    centertype: str | None = None,
    centermask: str | None = None,
    skip_novoxels: bool = False,
    all_labels: bool = False,
    all_keys: bool = False,
    lkeys: str | None = None,
    rkeys: str | None = None,
    klabel: str | None = None,
    match_label: str | None = None,
    labeltable_of_dset: InputPathType | None = None,
    word_label_match: bool = False,
    quiet_death: bool = False,
    lt_to_atlas_pl: str | None = None,
    dset_lt_to_atlas_pl: list[InputPathType] | None = None,
    lt_to_csv: InputPathType | None = None,
    atlasize_labeled_dset: InputPathType | None = None,
    atlas_file: str | None = None,
    atlas_name: str | None = None,
    atlas_description: str | None = None,
    replace: bool = False,
    add_atlas_dset: InputPathType | None = None,
    h_web: bool = False,
    h_view: bool = False,
    all_opts: bool = False,
    h_find: str | None = None,
    runner: Runner | None = None,
) -> VMakeLabelTableOutputs:
    """
    Script used to create, modify, and transform label tables.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        labeltable: Name of output label table.
        atlas_pointlist: Instead of a label table, produce an atlas point list.
        lab_r: Define a label with its minimum and maximum key values.
        lab_v: Define a label and its value.
        lab_file_delim: Set column delimiter for -lab_file option.
        lab_file: Specify labels and keys from a text file.
        dset: Attach the label table (or atlas point list) to dataset.
        longnames: Allow for another column of long names for regions.
        last_longname_col: Limit long names to nth column.
        centers: Compute center of mass location for each ROI.
        centertype: Different ways to compute centers (Icent, Dcent, cm).
        centermask: Calculate center of mass locations using a subset of voxels.
        skip_novoxels: Skip regions without voxels.
        all_labels: Return a listing of all labels.
        all_keys: Return a listing of all keys.
        lkeys: Return the keys whose labels match a given label.
        rkeys: Return the range (min max) of keys whose labels match a given\
            label.
        klabel: Return the label associated with a given key.
        match_label: Return labels matching a given label.
        labeltable_of_dset: Dump the labeltable from a dataset.
        word_label_match: Use word matching for labels.
        quiet_death: Do not give error messages when failing.
        lt_to_atlas_pl: Transform Label Table to Atlas Point List.
        dset_lt_to_atlas_pl: Get Label Table in dataset and write as an Atlas\
            Point List.
        lt_to_csv: Transform Label Table to CSV format.
        atlasize_labeled_dset: Transform a labeled ROI dataset into an atlas.
        atlas_file: Specify the name of the NIML file where atlas attributes\
            are stored.
        atlas_name: Name of the Atlas.
        atlas_description: Description of the Atlas, which appears in AFNI's\
            whereami window.
        replace: Replace existing Atlas if the name already exists in the NIML\
            file.
        add_atlas_dset: Add an existing atlas to an atlas file.
        h_web: Open webpage with help for this program.
        h_view: Open -help output in a GUI editor.
        all_opts: List all of the options for this script.
        h_find: Search for lines containing a specific word in the help output.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `VMakeLabelTableOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V__MAKE_LABEL_TABLE_METADATA)
    params = v__make_label_table_params(
        labeltable=labeltable,
        atlas_pointlist=atlas_pointlist,
        lab_r=lab_r,
        lab_v=lab_v,
        lab_file_delim=lab_file_delim,
        lab_file=lab_file,
        dset=dset,
        longnames=longnames,
        last_longname_col=last_longname_col,
        centers=centers,
        centertype=centertype,
        centermask=centermask,
        skip_novoxels=skip_novoxels,
        all_labels=all_labels,
        all_keys=all_keys,
        lkeys=lkeys,
        rkeys=rkeys,
        klabel=klabel,
        match_label=match_label,
        labeltable_of_dset=labeltable_of_dset,
        word_label_match=word_label_match,
        quiet_death=quiet_death,
        lt_to_atlas_pl=lt_to_atlas_pl,
        dset_lt_to_atlas_pl=dset_lt_to_atlas_pl,
        lt_to_csv=lt_to_csv,
        atlasize_labeled_dset=atlasize_labeled_dset,
        atlas_file=atlas_file,
        atlas_name=atlas_name,
        atlas_description=atlas_description,
        replace=replace,
        add_atlas_dset=add_atlas_dset,
        h_web=h_web,
        h_view=h_view,
        all_opts=all_opts,
        h_find=h_find,
    )
    return v__make_label_table_execute(params, execution)


__all__ = [
    "VMakeLabelTableOutputs",
    "VMakeLabelTableParameters",
    "V__MAKE_LABEL_TABLE_METADATA",
    "v__make_label_table",
    "v__make_label_table_params",
]
