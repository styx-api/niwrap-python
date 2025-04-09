# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

CIFTI_PALETTE_METADATA = Metadata(
    id="461f2ee9e43d09c23e5c231be5740676633ca913.boutiques",
    name="cifti-palette",
    package="workbench",
    container_image_tag="brainlife/connectome_workbench:1.5.0-freesurfer-update",
)


CiftiPalettePosPercentParameters = typing.TypedDict('CiftiPalettePosPercentParameters', {
    "__STYX_TYPE__": typing.Literal["pos_percent"],
    "pos_min__": float,
    "pos_max__": float,
})


CiftiPaletteNegPercentParameters = typing.TypedDict('CiftiPaletteNegPercentParameters', {
    "__STYX_TYPE__": typing.Literal["neg_percent"],
    "neg_min__": float,
    "neg_max__": float,
})


CiftiPalettePosUserParameters = typing.TypedDict('CiftiPalettePosUserParameters', {
    "__STYX_TYPE__": typing.Literal["pos_user"],
    "pos_min_user": float,
    "pos_max_user": float,
})


CiftiPaletteNegUserParameters = typing.TypedDict('CiftiPaletteNegUserParameters', {
    "__STYX_TYPE__": typing.Literal["neg_user"],
    "neg_min_user": float,
    "neg_max_user": float,
})


CiftiPaletteThresholdingParameters = typing.TypedDict('CiftiPaletteThresholdingParameters', {
    "__STYX_TYPE__": typing.Literal["thresholding"],
    "type": str,
    "test": str,
    "min": float,
    "max": float,
})


CiftiPaletteParameters = typing.TypedDict('CiftiPaletteParameters', {
    "__STYX_TYPE__": typing.Literal["cifti-palette"],
    "cifti_in": InputPathType,
    "mode": str,
    "cifti_out": str,
    "opt_column_column": typing.NotRequired[str | None],
    "pos_percent": typing.NotRequired[CiftiPalettePosPercentParameters | None],
    "neg_percent": typing.NotRequired[CiftiPaletteNegPercentParameters | None],
    "pos_user": typing.NotRequired[CiftiPalettePosUserParameters | None],
    "neg_user": typing.NotRequired[CiftiPaletteNegUserParameters | None],
    "opt_interpolate_interpolate": typing.NotRequired[typing.Literal["true", "false"] | None],
    "opt_disp_pos_display": typing.NotRequired[typing.Literal["true", "false"] | None],
    "opt_disp_neg_display": typing.NotRequired[typing.Literal["true", "false"] | None],
    "opt_disp_zero_display": typing.NotRequired[typing.Literal["true", "false"] | None],
    "opt_palette_name_name": typing.NotRequired[str | None],
    "thresholding": typing.NotRequired[CiftiPaletteThresholdingParameters | None],
    "opt_inversion_type": typing.NotRequired[str | None],
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
        "cifti-palette": cifti_palette_cargs,
        "pos_percent": cifti_palette_pos_percent_cargs,
        "neg_percent": cifti_palette_neg_percent_cargs,
        "pos_user": cifti_palette_pos_user_cargs,
        "neg_user": cifti_palette_neg_user_cargs,
        "thresholding": cifti_palette_thresholding_cargs,
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
        "cifti-palette": cifti_palette_outputs,
    }.get(t)


def cifti_palette_pos_percent_params(
    pos_min__: float,
    pos_max__: float,
) -> CiftiPalettePosPercentParameters:
    """
    Build parameters.
    
    Args:
        pos_min__: the percentile for the least positive data.
        pos_max__: the percentile for the most positive data.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "pos_percent",
        "pos_min__": pos_min__,
        "pos_max__": pos_max__,
    }
    return params


def cifti_palette_pos_percent_cargs(
    params: CiftiPalettePosPercentParameters,
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
    cargs.append("-pos-percent")
    cargs.append(str(params.get("pos_min__")))
    cargs.append(str(params.get("pos_max__")))
    return cargs


def cifti_palette_neg_percent_params(
    neg_min__: float,
    neg_max__: float,
) -> CiftiPaletteNegPercentParameters:
    """
    Build parameters.
    
    Args:
        neg_min__: the percentile for the least negative data.
        neg_max__: the percentile for the most negative data.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "neg_percent",
        "neg_min__": neg_min__,
        "neg_max__": neg_max__,
    }
    return params


def cifti_palette_neg_percent_cargs(
    params: CiftiPaletteNegPercentParameters,
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
    cargs.append("-neg-percent")
    cargs.append(str(params.get("neg_min__")))
    cargs.append(str(params.get("neg_max__")))
    return cargs


def cifti_palette_pos_user_params(
    pos_min_user: float,
    pos_max_user: float,
) -> CiftiPalettePosUserParameters:
    """
    Build parameters.
    
    Args:
        pos_min_user: the value for the least positive data.
        pos_max_user: the value for the most positive data.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "pos_user",
        "pos_min_user": pos_min_user,
        "pos_max_user": pos_max_user,
    }
    return params


def cifti_palette_pos_user_cargs(
    params: CiftiPalettePosUserParameters,
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
    cargs.append("-pos-user")
    cargs.append(str(params.get("pos_min_user")))
    cargs.append(str(params.get("pos_max_user")))
    return cargs


def cifti_palette_neg_user_params(
    neg_min_user: float,
    neg_max_user: float,
) -> CiftiPaletteNegUserParameters:
    """
    Build parameters.
    
    Args:
        neg_min_user: the value for the least negative data.
        neg_max_user: the value for the most negative data.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "neg_user",
        "neg_min_user": neg_min_user,
        "neg_max_user": neg_max_user,
    }
    return params


def cifti_palette_neg_user_cargs(
    params: CiftiPaletteNegUserParameters,
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
    cargs.append("-neg-user")
    cargs.append(str(params.get("neg_min_user")))
    cargs.append(str(params.get("neg_max_user")))
    return cargs


def cifti_palette_thresholding_params(
    type_: str,
    test: str,
    min_: float,
    max_: float,
) -> CiftiPaletteThresholdingParameters:
    """
    Build parameters.
    
    Args:
        type_: thresholding setting.
        test: show values inside or outside thresholds.
        min_: lower threshold.
        max_: upper threshold.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "thresholding",
        "type": type_,
        "test": test,
        "min": min_,
        "max": max_,
    }
    return params


def cifti_palette_thresholding_cargs(
    params: CiftiPaletteThresholdingParameters,
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
    cargs.append("-thresholding")
    cargs.append(params.get("type"))
    cargs.append(params.get("test"))
    cargs.append(str(params.get("min")))
    cargs.append(str(params.get("max")))
    return cargs


class CiftiPaletteOutputs(typing.NamedTuple):
    """
    Output object returned when calling `cifti_palette(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    cifti_out: OutputPathType
    """the output cifti file"""


def cifti_palette_params(
    cifti_in: InputPathType,
    mode: str,
    cifti_out: str,
    opt_column_column: str | None = None,
    pos_percent: CiftiPalettePosPercentParameters | None = None,
    neg_percent: CiftiPaletteNegPercentParameters | None = None,
    pos_user: CiftiPalettePosUserParameters | None = None,
    neg_user: CiftiPaletteNegUserParameters | None = None,
    opt_interpolate_interpolate: typing.Literal["true", "false"] | None = None,
    opt_disp_pos_display: typing.Literal["true", "false"] | None = None,
    opt_disp_neg_display: typing.Literal["true", "false"] | None = None,
    opt_disp_zero_display: typing.Literal["true", "false"] | None = None,
    opt_palette_name_name: str | None = None,
    thresholding: CiftiPaletteThresholdingParameters | None = None,
    opt_inversion_type: str | None = None,
) -> CiftiPaletteParameters:
    """
    Build parameters.
    
    Args:
        cifti_in: the cifti input.
        mode: the mapping mode.
        cifti_out: the output cifti file.
        opt_column_column: select a single column for scalar maps: the column\
            number or name.
        pos_percent: percentage min/max for positive data coloring.
        neg_percent: percentage min/max for negative data coloring.
        pos_user: user min/max values for positive data coloring.
        neg_user: user min/max values for negative data coloring.
        opt_interpolate_interpolate: interpolate colors: boolean, whether to\
            interpolate.
        opt_disp_pos_display: display positive data: boolean, whether to\
            display.
        opt_disp_neg_display: display positive data: boolean, whether to\
            display.
        opt_disp_zero_display: display data closer to zero than the min cutoff:\
            boolean, whether to display.
        opt_palette_name_name: set the palette used: the name of the palette.
        thresholding: set the thresholding.
        opt_inversion_type: specify palette inversion: the type of inversion.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "cifti-palette",
        "cifti_in": cifti_in,
        "mode": mode,
        "cifti_out": cifti_out,
    }
    if opt_column_column is not None:
        params["opt_column_column"] = opt_column_column
    if pos_percent is not None:
        params["pos_percent"] = pos_percent
    if neg_percent is not None:
        params["neg_percent"] = neg_percent
    if pos_user is not None:
        params["pos_user"] = pos_user
    if neg_user is not None:
        params["neg_user"] = neg_user
    if opt_interpolate_interpolate is not None:
        params["opt_interpolate_interpolate"] = opt_interpolate_interpolate
    if opt_disp_pos_display is not None:
        params["opt_disp_pos_display"] = opt_disp_pos_display
    if opt_disp_neg_display is not None:
        params["opt_disp_neg_display"] = opt_disp_neg_display
    if opt_disp_zero_display is not None:
        params["opt_disp_zero_display"] = opt_disp_zero_display
    if opt_palette_name_name is not None:
        params["opt_palette_name_name"] = opt_palette_name_name
    if thresholding is not None:
        params["thresholding"] = thresholding
    if opt_inversion_type is not None:
        params["opt_inversion_type"] = opt_inversion_type
    return params


def cifti_palette_cargs(
    params: CiftiPaletteParameters,
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
    cargs.append("wb_command")
    cargs.append("-cifti-palette")
    cargs.append(execution.input_file(params.get("cifti_in")))
    cargs.append(params.get("mode"))
    cargs.append(params.get("cifti_out"))
    if params.get("opt_column_column") is not None:
        cargs.extend([
            "-column",
            params.get("opt_column_column")
        ])
    if params.get("pos_percent") is not None:
        cargs.extend(dyn_cargs(params.get("pos_percent")["__STYXTYPE__"])(params.get("pos_percent"), execution))
    if params.get("neg_percent") is not None:
        cargs.extend(dyn_cargs(params.get("neg_percent")["__STYXTYPE__"])(params.get("neg_percent"), execution))
    if params.get("pos_user") is not None:
        cargs.extend(dyn_cargs(params.get("pos_user")["__STYXTYPE__"])(params.get("pos_user"), execution))
    if params.get("neg_user") is not None:
        cargs.extend(dyn_cargs(params.get("neg_user")["__STYXTYPE__"])(params.get("neg_user"), execution))
    if params.get("opt_interpolate_interpolate") is not None:
        cargs.extend([
            "-interpolate",
            params.get("opt_interpolate_interpolate")
        ])
    if params.get("opt_disp_pos_display") is not None:
        cargs.extend([
            "-disp-pos",
            params.get("opt_disp_pos_display")
        ])
    if params.get("opt_disp_neg_display") is not None:
        cargs.extend([
            "-disp-neg",
            params.get("opt_disp_neg_display")
        ])
    if params.get("opt_disp_zero_display") is not None:
        cargs.extend([
            "-disp-zero",
            params.get("opt_disp_zero_display")
        ])
    if params.get("opt_palette_name_name") is not None:
        cargs.extend([
            "-palette-name",
            params.get("opt_palette_name_name")
        ])
    if params.get("thresholding") is not None:
        cargs.extend(dyn_cargs(params.get("thresholding")["__STYXTYPE__"])(params.get("thresholding"), execution))
    if params.get("opt_inversion_type") is not None:
        cargs.extend([
            "-inversion",
            params.get("opt_inversion_type")
        ])
    return cargs


def cifti_palette_outputs(
    params: CiftiPaletteParameters,
    execution: Execution,
) -> CiftiPaletteOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = CiftiPaletteOutputs(
        root=execution.output_file("."),
        cifti_out=execution.output_file(params.get("cifti_out")),
    )
    return ret


def cifti_palette_execute(
    params: CiftiPaletteParameters,
    execution: Execution,
) -> CiftiPaletteOutputs:
    """
    Set palette on a cifti file.
    
    NOTE: The output file must be a different file than the input file.
    
    For scalar maps, by default the palette is changed for every map, specify
    -column to change only one map. Palette settings not specified will be taken
    from the first column for scalar maps, and from the existing file palette
    for other mapping types. The <mode> argument must be one of the following:
    
    MODE_AUTO_SCALE
    MODE_AUTO_SCALE_ABSOLUTE_PERCENTAGE
    MODE_AUTO_SCALE_PERCENTAGE
    MODE_USER_SCALE
    
    The <name> argument to -palette-name must be one of the following:
    
    ROY-BIG-BL
    videen_style
    Gray_Interp_Positive
    Gray_Interp
    PSYCH-FIXED
    RBGYR20
    RBGYR20P
    RYGBR4_positive
    RGRBR_mirror90_pos
    Orange-Yellow
    POS_NEG_ZERO
    red-yellow
    blue-lightblue
    FSL
    power_surf
    black-red
    black-green
    black-blue
    black-red-positive
    black-green-positive
    black-blue-positive
    blue-black-green
    blue-black-red
    red-black-green
    fsl_red
    fsl_green
    fsl_blue
    fsl_yellow
    RedWhiteBlue
    cool-warm
    spectral
    RY-BC-BL
    magma
    JET256
    PSYCH
    PSYCH-NO-NONE
    ROY-BIG
    clear_brain
    fidl
    raich4_clrmid
    raich6_clrmid
    HSB8_clrmid
    POS_NEG
    Special-RGB-Volume
    
    The <type> argument to -thresholding must be one of the following:
    
    THRESHOLD_TYPE_OFF
    THRESHOLD_TYPE_NORMAL
    THRESHOLD_TYPE_FILE
    
    The <test> argument to -thresholding must be one of the following:
    
    THRESHOLD_TEST_SHOW_OUTSIDE
    THRESHOLD_TEST_SHOW_INSIDE
    
    The <type> argument to -inversion must be one of the following:
    
    OFF
    POSITIVE_WITH_NEGATIVE
    POSITIVE_NEGATIVE_SEPARATE
    .
    
    Author: Connectome Workbench Developers
    
    URL: https://github.com/Washington-University/workbench
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `CiftiPaletteOutputs`).
    """
    params = execution.params(params)
    cargs = cifti_palette_cargs(params, execution)
    ret = cifti_palette_outputs(params, execution)
    execution.run(cargs)
    return ret


def cifti_palette(
    cifti_in: InputPathType,
    mode: str,
    cifti_out: str,
    opt_column_column: str | None = None,
    pos_percent: CiftiPalettePosPercentParameters | None = None,
    neg_percent: CiftiPaletteNegPercentParameters | None = None,
    pos_user: CiftiPalettePosUserParameters | None = None,
    neg_user: CiftiPaletteNegUserParameters | None = None,
    opt_interpolate_interpolate: typing.Literal["true", "false"] | None = None,
    opt_disp_pos_display: typing.Literal["true", "false"] | None = None,
    opt_disp_neg_display: typing.Literal["true", "false"] | None = None,
    opt_disp_zero_display: typing.Literal["true", "false"] | None = None,
    opt_palette_name_name: str | None = None,
    thresholding: CiftiPaletteThresholdingParameters | None = None,
    opt_inversion_type: str | None = None,
    runner: Runner | None = None,
) -> CiftiPaletteOutputs:
    """
    Set palette on a cifti file.
    
    NOTE: The output file must be a different file than the input file.
    
    For scalar maps, by default the palette is changed for every map, specify
    -column to change only one map. Palette settings not specified will be taken
    from the first column for scalar maps, and from the existing file palette
    for other mapping types. The <mode> argument must be one of the following:
    
    MODE_AUTO_SCALE
    MODE_AUTO_SCALE_ABSOLUTE_PERCENTAGE
    MODE_AUTO_SCALE_PERCENTAGE
    MODE_USER_SCALE
    
    The <name> argument to -palette-name must be one of the following:
    
    ROY-BIG-BL
    videen_style
    Gray_Interp_Positive
    Gray_Interp
    PSYCH-FIXED
    RBGYR20
    RBGYR20P
    RYGBR4_positive
    RGRBR_mirror90_pos
    Orange-Yellow
    POS_NEG_ZERO
    red-yellow
    blue-lightblue
    FSL
    power_surf
    black-red
    black-green
    black-blue
    black-red-positive
    black-green-positive
    black-blue-positive
    blue-black-green
    blue-black-red
    red-black-green
    fsl_red
    fsl_green
    fsl_blue
    fsl_yellow
    RedWhiteBlue
    cool-warm
    spectral
    RY-BC-BL
    magma
    JET256
    PSYCH
    PSYCH-NO-NONE
    ROY-BIG
    clear_brain
    fidl
    raich4_clrmid
    raich6_clrmid
    HSB8_clrmid
    POS_NEG
    Special-RGB-Volume
    
    The <type> argument to -thresholding must be one of the following:
    
    THRESHOLD_TYPE_OFF
    THRESHOLD_TYPE_NORMAL
    THRESHOLD_TYPE_FILE
    
    The <test> argument to -thresholding must be one of the following:
    
    THRESHOLD_TEST_SHOW_OUTSIDE
    THRESHOLD_TEST_SHOW_INSIDE
    
    The <type> argument to -inversion must be one of the following:
    
    OFF
    POSITIVE_WITH_NEGATIVE
    POSITIVE_NEGATIVE_SEPARATE
    .
    
    Author: Connectome Workbench Developers
    
    URL: https://github.com/Washington-University/workbench
    
    Args:
        cifti_in: the cifti input.
        mode: the mapping mode.
        cifti_out: the output cifti file.
        opt_column_column: select a single column for scalar maps: the column\
            number or name.
        pos_percent: percentage min/max for positive data coloring.
        neg_percent: percentage min/max for negative data coloring.
        pos_user: user min/max values for positive data coloring.
        neg_user: user min/max values for negative data coloring.
        opt_interpolate_interpolate: interpolate colors: boolean, whether to\
            interpolate.
        opt_disp_pos_display: display positive data: boolean, whether to\
            display.
        opt_disp_neg_display: display positive data: boolean, whether to\
            display.
        opt_disp_zero_display: display data closer to zero than the min cutoff:\
            boolean, whether to display.
        opt_palette_name_name: set the palette used: the name of the palette.
        thresholding: set the thresholding.
        opt_inversion_type: specify palette inversion: the type of inversion.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `CiftiPaletteOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(CIFTI_PALETTE_METADATA)
    params = cifti_palette_params(
        cifti_in=cifti_in,
        mode=mode,
        cifti_out=cifti_out,
        opt_column_column=opt_column_column,
        pos_percent=pos_percent,
        neg_percent=neg_percent,
        pos_user=pos_user,
        neg_user=neg_user,
        opt_interpolate_interpolate=opt_interpolate_interpolate,
        opt_disp_pos_display=opt_disp_pos_display,
        opt_disp_neg_display=opt_disp_neg_display,
        opt_disp_zero_display=opt_disp_zero_display,
        opt_palette_name_name=opt_palette_name_name,
        thresholding=thresholding,
        opt_inversion_type=opt_inversion_type,
    )
    return cifti_palette_execute(params, execution)


__all__ = [
    "CIFTI_PALETTE_METADATA",
    "CiftiPaletteNegPercentParameters",
    "CiftiPaletteNegUserParameters",
    "CiftiPaletteOutputs",
    "CiftiPaletteParameters",
    "CiftiPalettePosPercentParameters",
    "CiftiPalettePosUserParameters",
    "CiftiPaletteThresholdingParameters",
    "cifti_palette",
    "cifti_palette_neg_percent_params",
    "cifti_palette_neg_user_params",
    "cifti_palette_params",
    "cifti_palette_pos_percent_params",
    "cifti_palette_pos_user_params",
    "cifti_palette_thresholding_params",
]
