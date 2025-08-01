# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

V_3D_ANOVA3_METADATA = Metadata(
    id="1e464f155335b3c9815ddb43161916b9ff1a4fe2.boutiques",
    name="3dANOVA3",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


V3dAnova3OutfileAbcontrParameters = typing.TypedDict('V3dAnova3OutfileAbcontrParameters', {
    "__STYXTYPE__": typing.Literal["outfile_abcontr"],
    "outfile_abcontr": typing.NotRequired[str | None],
    "outfile_Abcontr": typing.NotRequired[str | None],
})


V3dAnova3OutfileAbcontr1Parameters = typing.TypedDict('V3dAnova3OutfileAbcontr1Parameters', {
    "__STYXTYPE__": typing.Literal["outfile_abcontr_1"],
    "outfile_abdiff": typing.NotRequired[str | None],
    "outfile_Abdiff": typing.NotRequired[str | None],
})


V3dAnova3Parameters = typing.TypedDict('V3dAnova3Parameters', {
    "__STYXTYPE__": typing.Literal["3dANOVA3"],
    "type": int,
    "alevels": int,
    "blevels": int,
    "clevels": int,
    "dsets": list[str],
    "voxel_num": typing.NotRequired[int | None],
    "diskspace": bool,
    "mask": typing.NotRequired[InputPathType | None],
    "outfile_fa": typing.NotRequired[str | None],
    "outfile_fb": typing.NotRequired[str | None],
    "outfile_fc": typing.NotRequired[str | None],
    "outfile_fab": typing.NotRequired[str | None],
    "outfile_fac": typing.NotRequired[str | None],
    "outfile_fbc": typing.NotRequired[str | None],
    "outfile_fabc": typing.NotRequired[str | None],
    "outfile_amean": typing.NotRequired[str | None],
    "outfile_bmean": typing.NotRequired[str | None],
    "outfile_cmean": typing.NotRequired[str | None],
    "outfile_xmean": typing.NotRequired[str | None],
    "outfile_adiff": typing.NotRequired[str | None],
    "outfile_bdiff": typing.NotRequired[str | None],
    "outfile_cdiff": typing.NotRequired[str | None],
    "outfile_xdiff": typing.NotRequired[str | None],
    "outfile_acontr": typing.NotRequired[str | None],
    "outfile_bcontr": typing.NotRequired[str | None],
    "outfile_ccontr": typing.NotRequired[str | None],
    "outfile_abcontr": typing.NotRequired[V3dAnova3OutfileAbcontrParameters | None],
    "outfile_abdiff": typing.NotRequired[V3dAnova3OutfileAbcontr1Parameters | None],
    "outfile_abmean": typing.NotRequired[str | None],
    "outfile_bucket": typing.NotRequired[str | None],
    "anova_options": typing.NotRequired[list[str] | None],
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
        "3dANOVA3": v_3d_anova3_cargs,
        "outfile_abcontr": v_3d_anova3_outfile_abcontr_cargs,
        "outfile_abcontr_1": v_3d_anova3_outfile_abcontr_1_cargs,
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
        "3dANOVA3": v_3d_anova3_outputs,
    }.get(t)


def v_3d_anova3_outfile_abcontr_params(
    outfile_abcontr: str | None = None,
    outfile_abcontr_: str | None = None,
) -> V3dAnova3OutfileAbcontrParameters:
    """
    Build parameters.
    
    Args:
        outfile_abcontr: Specify the output file for the interaction contrast\
            results between A and B.
        outfile_abcontr_: Specify the output file for the interaction contrast\
            results between A and B (case-sensitive).
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "outfile_abcontr",
    }
    if outfile_abcontr is not None:
        params["outfile_abcontr"] = outfile_abcontr
    if outfile_abcontr_ is not None:
        params["outfile_Abcontr"] = outfile_abcontr_
    return params


def v_3d_anova3_outfile_abcontr_cargs(
    params: V3dAnova3OutfileAbcontrParameters,
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
    if params.get("outfile_abcontr") is not None:
        cargs.extend([
            "-aBcontr",
            params.get("outfile_abcontr")
        ])
    if params.get("outfile_Abcontr") is not None:
        cargs.extend([
            "-Abcontr",
            params.get("outfile_Abcontr")
        ])
    return cargs


def v_3d_anova3_outfile_abcontr_1_params(
    outfile_abdiff: str | None = None,
    outfile_abdiff_: str | None = None,
) -> V3dAnova3OutfileAbcontr1Parameters:
    """
    Build parameters.
    
    Args:
        outfile_abdiff: Specify the output file for the interaction difference\
            results between A and B.
        outfile_abdiff_: Specify the output file for the interaction difference\
            results between A and B (case-sensitive).
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "outfile_abcontr_1",
    }
    if outfile_abdiff is not None:
        params["outfile_abdiff"] = outfile_abdiff
    if outfile_abdiff_ is not None:
        params["outfile_Abdiff"] = outfile_abdiff_
    return params


def v_3d_anova3_outfile_abcontr_1_cargs(
    params: V3dAnova3OutfileAbcontr1Parameters,
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
    if params.get("outfile_abdiff") is not None:
        cargs.extend([
            "-aBdiff",
            params.get("outfile_abdiff")
        ])
    if params.get("outfile_Abdiff") is not None:
        cargs.extend([
            "-Abdiff",
            params.get("outfile_Abdiff")
        ])
    return cargs


class V3dAnova3Outputs(typing.NamedTuple):
    """
    Output object returned when calling `v_3d_anova3(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    outfile_fa: OutputPathType | None
    """Output file for the main ANOVA result."""
    outfile_fb: OutputPathType | None
    """Output file for the main B ANOVA result."""
    outfile_fc: OutputPathType | None
    """Output file for the main C ANOVA result."""
    outfile_fab: OutputPathType | None
    """Output file for the interaction between A and B."""
    outfile_fac: OutputPathType | None
    """Output file for the interaction between A and C."""
    outfile_fbc: OutputPathType | None
    """Output file for the interaction between B and C."""
    outfile_fabc: OutputPathType | None
    """Output file for the interaction between A, B, and C."""
    outfile_amean: OutputPathType | None
    """Output file for the A mean results."""
    outfile_bmean: OutputPathType | None
    """Output file for the B mean results."""


def v_3d_anova3_params(
    type_: int,
    alevels: int,
    blevels: int,
    clevels: int,
    dsets: list[str],
    voxel_num: int | None = None,
    diskspace: bool = False,
    mask: InputPathType | None = None,
    outfile_fa: str | None = None,
    outfile_fb: str | None = None,
    outfile_fc: str | None = None,
    outfile_fab: str | None = None,
    outfile_fac: str | None = None,
    outfile_fbc: str | None = None,
    outfile_fabc: str | None = None,
    outfile_amean: str | None = None,
    outfile_bmean: str | None = None,
    outfile_cmean: str | None = None,
    outfile_xmean: str | None = None,
    outfile_adiff: str | None = None,
    outfile_bdiff: str | None = None,
    outfile_cdiff: str | None = None,
    outfile_xdiff: str | None = None,
    outfile_acontr: str | None = None,
    outfile_bcontr: str | None = None,
    outfile_ccontr: str | None = None,
    outfile_abcontr: V3dAnova3OutfileAbcontrParameters | None = None,
    outfile_abdiff: V3dAnova3OutfileAbcontr1Parameters | None = None,
    outfile_abmean: str | None = None,
    outfile_bucket: str | None = None,
    anova_options: list[str] | None = None,
) -> V3dAnova3Parameters:
    """
    Build parameters.
    
    Args:
        type_: Type of ANOVA model to be used. k = 1: A,B,C fixed; AxBxC, k =\
            2: A,B,C random; AxBxC, k = 3: A fixed; B,C random; AxBxC, k = 4: A,B\
            fixed; C random; AxBxC, k = 5: A,B fixed; C random; AxB,BxC,C(A).
        alevels: Number of levels for factor A.
        blevels: Number of levels for factor B.
        clevels: Number of levels for factor C.
        dsets: Input data sets for specific levels of factors A, B, and C.
        voxel_num: Screen output for specified voxel number.
        diskspace: Print out disk space required for program execution.
        mask: Use sub-brick #0 of dataset to define which voxels to process.
        outfile_fa: Specify the output file for the main ANOVA result.
        outfile_fb: Specify the output file for the main B ANOVA result.
        outfile_fc: Specify the output file for the main C ANOVA result.
        outfile_fab: Specify the output file for the interaction between A and\
            B.
        outfile_fac: Specify the output file for the interaction between A and\
            C.
        outfile_fbc: Specify the output file for the interaction between B and\
            C.
        outfile_fabc: Specify the output file for the interaction between A, B,\
            and C.
        outfile_amean: Specify the output file for the A mean results.
        outfile_bmean: Specify the output file for the B mean results.
        outfile_cmean: Specify the output file for the C mean results.
        outfile_xmean: Specify the output file for the overall mean results.
        outfile_adiff: Specify the output file for the A difference results.
        outfile_bdiff: Specify the output file for the B difference results.
        outfile_cdiff: Specify the output file for the C difference results.
        outfile_xdiff: Specify the output file for the overall difference\
            results.
        outfile_acontr: Specify the output file for the A contrast results.
        outfile_bcontr: Specify the output file for the B contrast results.
        outfile_ccontr: Specify the output file for the C contrast results.
        outfile_abcontr: Specify the output file for the interaction contrast\
            results between A and B.
        outfile_abdiff: Specify the output file for the interaction contrast\
            results between A and B.
        outfile_abmean: Specify the output file for the mean results of the\
            interaction between A and B.
        outfile_bucket: Specify the output file for the bucket (combined)\
            results.
        anova_options: Modified ANOVA computation options. See:\
            https://afni.nimh.nih.gov/sscc/gangc/ANOVA_Mod.html.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "3dANOVA3",
        "type": type_,
        "alevels": alevels,
        "blevels": blevels,
        "clevels": clevels,
        "dsets": dsets,
        "diskspace": diskspace,
    }
    if voxel_num is not None:
        params["voxel_num"] = voxel_num
    if mask is not None:
        params["mask"] = mask
    if outfile_fa is not None:
        params["outfile_fa"] = outfile_fa
    if outfile_fb is not None:
        params["outfile_fb"] = outfile_fb
    if outfile_fc is not None:
        params["outfile_fc"] = outfile_fc
    if outfile_fab is not None:
        params["outfile_fab"] = outfile_fab
    if outfile_fac is not None:
        params["outfile_fac"] = outfile_fac
    if outfile_fbc is not None:
        params["outfile_fbc"] = outfile_fbc
    if outfile_fabc is not None:
        params["outfile_fabc"] = outfile_fabc
    if outfile_amean is not None:
        params["outfile_amean"] = outfile_amean
    if outfile_bmean is not None:
        params["outfile_bmean"] = outfile_bmean
    if outfile_cmean is not None:
        params["outfile_cmean"] = outfile_cmean
    if outfile_xmean is not None:
        params["outfile_xmean"] = outfile_xmean
    if outfile_adiff is not None:
        params["outfile_adiff"] = outfile_adiff
    if outfile_bdiff is not None:
        params["outfile_bdiff"] = outfile_bdiff
    if outfile_cdiff is not None:
        params["outfile_cdiff"] = outfile_cdiff
    if outfile_xdiff is not None:
        params["outfile_xdiff"] = outfile_xdiff
    if outfile_acontr is not None:
        params["outfile_acontr"] = outfile_acontr
    if outfile_bcontr is not None:
        params["outfile_bcontr"] = outfile_bcontr
    if outfile_ccontr is not None:
        params["outfile_ccontr"] = outfile_ccontr
    if outfile_abcontr is not None:
        params["outfile_abcontr"] = outfile_abcontr
    if outfile_abdiff is not None:
        params["outfile_abdiff"] = outfile_abdiff
    if outfile_abmean is not None:
        params["outfile_abmean"] = outfile_abmean
    if outfile_bucket is not None:
        params["outfile_bucket"] = outfile_bucket
    if anova_options is not None:
        params["anova_options"] = anova_options
    return params


def v_3d_anova3_cargs(
    params: V3dAnova3Parameters,
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
    cargs.append("3dANOVA3")
    cargs.extend([
        "-type",
        str(params.get("type"))
    ])
    cargs.extend([
        "-alevels",
        str(params.get("alevels"))
    ])
    cargs.extend([
        "-blevels",
        str(params.get("blevels"))
    ])
    cargs.extend([
        "-clevels",
        str(params.get("clevels"))
    ])
    cargs.extend([
        "-dset",
        *params.get("dsets")
    ])
    if params.get("voxel_num") is not None:
        cargs.extend([
            "-voxel",
            str(params.get("voxel_num"))
        ])
    if params.get("diskspace"):
        cargs.append("-diskspace")
    if params.get("mask") is not None:
        cargs.extend([
            "-mask",
            execution.input_file(params.get("mask"))
        ])
    if params.get("outfile_fa") is not None:
        cargs.extend([
            "-fa",
            params.get("outfile_fa")
        ])
    if params.get("outfile_fb") is not None:
        cargs.extend([
            "-fb",
            params.get("outfile_fb")
        ])
    if params.get("outfile_fc") is not None:
        cargs.extend([
            "-fc",
            params.get("outfile_fc")
        ])
    if params.get("outfile_fab") is not None:
        cargs.extend([
            "-fab",
            params.get("outfile_fab")
        ])
    if params.get("outfile_fac") is not None:
        cargs.extend([
            "-fac",
            params.get("outfile_fac")
        ])
    if params.get("outfile_fbc") is not None:
        cargs.extend([
            "-fbc",
            params.get("outfile_fbc")
        ])
    if params.get("outfile_fabc") is not None:
        cargs.extend([
            "-fabc",
            params.get("outfile_fabc")
        ])
    if params.get("outfile_amean") is not None:
        cargs.extend([
            "-amean",
            params.get("outfile_amean")
        ])
    if params.get("outfile_bmean") is not None:
        cargs.extend([
            "-bmean",
            params.get("outfile_bmean")
        ])
    if params.get("outfile_cmean") is not None:
        cargs.extend([
            "-cmean",
            params.get("outfile_cmean")
        ])
    if params.get("outfile_xmean") is not None:
        cargs.extend([
            "-xmean",
            params.get("outfile_xmean")
        ])
    if params.get("outfile_adiff") is not None:
        cargs.extend([
            "-adiff",
            params.get("outfile_adiff")
        ])
    if params.get("outfile_bdiff") is not None:
        cargs.extend([
            "-bdiff",
            params.get("outfile_bdiff")
        ])
    if params.get("outfile_cdiff") is not None:
        cargs.extend([
            "-cdiff",
            params.get("outfile_cdiff")
        ])
    if params.get("outfile_xdiff") is not None:
        cargs.extend([
            "-xdiff",
            params.get("outfile_xdiff")
        ])
    if params.get("outfile_acontr") is not None:
        cargs.extend([
            "-acontr",
            params.get("outfile_acontr")
        ])
    if params.get("outfile_bcontr") is not None:
        cargs.extend([
            "-bcontr",
            params.get("outfile_bcontr")
        ])
    if params.get("outfile_ccontr") is not None:
        cargs.extend([
            "-ccontr",
            params.get("outfile_ccontr")
        ])
    if params.get("outfile_abcontr") is not None:
        cargs.extend(dyn_cargs(params.get("outfile_abcontr")["__STYXTYPE__"])(params.get("outfile_abcontr"), execution))
    if params.get("outfile_abdiff") is not None:
        cargs.extend(dyn_cargs(params.get("outfile_abdiff")["__STYXTYPE__"])(params.get("outfile_abdiff"), execution))
    if params.get("outfile_abmean") is not None:
        cargs.extend([
            "-abmean",
            params.get("outfile_abmean")
        ])
    if params.get("outfile_bucket") is not None:
        cargs.extend([
            "-bucket",
            params.get("outfile_bucket")
        ])
    if params.get("anova_options") is not None:
        cargs.extend([
            "-old_method -OK -assume_sph",
            *params.get("anova_options")
        ])
    return cargs


def v_3d_anova3_outputs(
    params: V3dAnova3Parameters,
    execution: Execution,
) -> V3dAnova3Outputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = V3dAnova3Outputs(
        root=execution.output_file("."),
        outfile_fa=execution.output_file(params.get("outfile_fa")) if (params.get("outfile_fa") is not None) else None,
        outfile_fb=execution.output_file(params.get("outfile_fb")) if (params.get("outfile_fb") is not None) else None,
        outfile_fc=execution.output_file(params.get("outfile_fc")) if (params.get("outfile_fc") is not None) else None,
        outfile_fab=execution.output_file(params.get("outfile_fab")) if (params.get("outfile_fab") is not None) else None,
        outfile_fac=execution.output_file(params.get("outfile_fac")) if (params.get("outfile_fac") is not None) else None,
        outfile_fbc=execution.output_file(params.get("outfile_fbc")) if (params.get("outfile_fbc") is not None) else None,
        outfile_fabc=execution.output_file(params.get("outfile_fabc")) if (params.get("outfile_fabc") is not None) else None,
        outfile_amean=execution.output_file(params.get("outfile_amean")) if (params.get("outfile_amean") is not None) else None,
        outfile_bmean=execution.output_file(params.get("outfile_bmean")) if (params.get("outfile_bmean") is not None) else None,
    )
    return ret


def v_3d_anova3_execute(
    params: V3dAnova3Parameters,
    execution: Execution,
) -> V3dAnova3Outputs:
    """
    Performs three-factor ANOVA on 3D data sets.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `V3dAnova3Outputs`).
    """
    params = execution.params(params)
    cargs = v_3d_anova3_cargs(params, execution)
    ret = v_3d_anova3_outputs(params, execution)
    execution.run(cargs)
    return ret


def v_3d_anova3(
    type_: int,
    alevels: int,
    blevels: int,
    clevels: int,
    dsets: list[str],
    voxel_num: int | None = None,
    diskspace: bool = False,
    mask: InputPathType | None = None,
    outfile_fa: str | None = None,
    outfile_fb: str | None = None,
    outfile_fc: str | None = None,
    outfile_fab: str | None = None,
    outfile_fac: str | None = None,
    outfile_fbc: str | None = None,
    outfile_fabc: str | None = None,
    outfile_amean: str | None = None,
    outfile_bmean: str | None = None,
    outfile_cmean: str | None = None,
    outfile_xmean: str | None = None,
    outfile_adiff: str | None = None,
    outfile_bdiff: str | None = None,
    outfile_cdiff: str | None = None,
    outfile_xdiff: str | None = None,
    outfile_acontr: str | None = None,
    outfile_bcontr: str | None = None,
    outfile_ccontr: str | None = None,
    outfile_abcontr: V3dAnova3OutfileAbcontrParameters | None = None,
    outfile_abdiff: V3dAnova3OutfileAbcontr1Parameters | None = None,
    outfile_abmean: str | None = None,
    outfile_bucket: str | None = None,
    anova_options: list[str] | None = None,
    runner: Runner | None = None,
) -> V3dAnova3Outputs:
    """
    Performs three-factor ANOVA on 3D data sets.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        type_: Type of ANOVA model to be used. k = 1: A,B,C fixed; AxBxC, k =\
            2: A,B,C random; AxBxC, k = 3: A fixed; B,C random; AxBxC, k = 4: A,B\
            fixed; C random; AxBxC, k = 5: A,B fixed; C random; AxB,BxC,C(A).
        alevels: Number of levels for factor A.
        blevels: Number of levels for factor B.
        clevels: Number of levels for factor C.
        dsets: Input data sets for specific levels of factors A, B, and C.
        voxel_num: Screen output for specified voxel number.
        diskspace: Print out disk space required for program execution.
        mask: Use sub-brick #0 of dataset to define which voxels to process.
        outfile_fa: Specify the output file for the main ANOVA result.
        outfile_fb: Specify the output file for the main B ANOVA result.
        outfile_fc: Specify the output file for the main C ANOVA result.
        outfile_fab: Specify the output file for the interaction between A and\
            B.
        outfile_fac: Specify the output file for the interaction between A and\
            C.
        outfile_fbc: Specify the output file for the interaction between B and\
            C.
        outfile_fabc: Specify the output file for the interaction between A, B,\
            and C.
        outfile_amean: Specify the output file for the A mean results.
        outfile_bmean: Specify the output file for the B mean results.
        outfile_cmean: Specify the output file for the C mean results.
        outfile_xmean: Specify the output file for the overall mean results.
        outfile_adiff: Specify the output file for the A difference results.
        outfile_bdiff: Specify the output file for the B difference results.
        outfile_cdiff: Specify the output file for the C difference results.
        outfile_xdiff: Specify the output file for the overall difference\
            results.
        outfile_acontr: Specify the output file for the A contrast results.
        outfile_bcontr: Specify the output file for the B contrast results.
        outfile_ccontr: Specify the output file for the C contrast results.
        outfile_abcontr: Specify the output file for the interaction contrast\
            results between A and B.
        outfile_abdiff: Specify the output file for the interaction contrast\
            results between A and B.
        outfile_abmean: Specify the output file for the mean results of the\
            interaction between A and B.
        outfile_bucket: Specify the output file for the bucket (combined)\
            results.
        anova_options: Modified ANOVA computation options. See:\
            https://afni.nimh.nih.gov/sscc/gangc/ANOVA_Mod.html.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V3dAnova3Outputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_3D_ANOVA3_METADATA)
    params = v_3d_anova3_params(
        type_=type_,
        alevels=alevels,
        blevels=blevels,
        clevels=clevels,
        dsets=dsets,
        voxel_num=voxel_num,
        diskspace=diskspace,
        mask=mask,
        outfile_fa=outfile_fa,
        outfile_fb=outfile_fb,
        outfile_fc=outfile_fc,
        outfile_fab=outfile_fab,
        outfile_fac=outfile_fac,
        outfile_fbc=outfile_fbc,
        outfile_fabc=outfile_fabc,
        outfile_amean=outfile_amean,
        outfile_bmean=outfile_bmean,
        outfile_cmean=outfile_cmean,
        outfile_xmean=outfile_xmean,
        outfile_adiff=outfile_adiff,
        outfile_bdiff=outfile_bdiff,
        outfile_cdiff=outfile_cdiff,
        outfile_xdiff=outfile_xdiff,
        outfile_acontr=outfile_acontr,
        outfile_bcontr=outfile_bcontr,
        outfile_ccontr=outfile_ccontr,
        outfile_abcontr=outfile_abcontr,
        outfile_abdiff=outfile_abdiff,
        outfile_abmean=outfile_abmean,
        outfile_bucket=outfile_bucket,
        anova_options=anova_options,
    )
    return v_3d_anova3_execute(params, execution)


__all__ = [
    "V3dAnova3OutfileAbcontr1Parameters",
    "V3dAnova3OutfileAbcontrParameters",
    "V3dAnova3Outputs",
    "V3dAnova3Parameters",
    "V_3D_ANOVA3_METADATA",
    "v_3d_anova3",
    "v_3d_anova3_outfile_abcontr_1_params",
    "v_3d_anova3_outfile_abcontr_params",
    "v_3d_anova3_params",
]
