# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

MBA_METADATA = Metadata(
    id="f8f6f30c2f9a76d32aa2209cf855c9214666a8bc.boutiques",
    name="MBA",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


MbaParameters = typing.TypedDict('MbaParameters', {
    "__STYXTYPE__": typing.Literal["MBA"],
    "prefix": str,
    "chains": typing.NotRequired[int | None],
    "iterations": typing.NotRequired[int | None],
    "model": typing.NotRequired[str | None],
    "eoi": typing.NotRequired[str | None],
    "data_table": InputPathType,
    "cvars": typing.NotRequired[str | None],
    "qvars": typing.NotRequired[str | None],
    "qcvar": typing.NotRequired[str | None],
    "stdz": typing.NotRequired[str | None],
    "wcp": typing.NotRequired[int | None],
    "disty": typing.NotRequired[str | None],
    "se": typing.NotRequired[str | None],
    "dbgArgs": bool,
    "help": bool,
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
        "MBA": mba_cargs,
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
        "MBA": mba_outputs,
    }.get(t)


class MbaOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mba(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_txt: OutputPathType
    """Main output text file storing inference information"""
    output_rdata: OutputPathType
    """R data file for post hoc processing and plotting"""
    matrix_plot: OutputPathType
    """Matrix plot visualization of analysis"""


def mba_params(
    prefix: str,
    data_table: InputPathType,
    chains: int | None = None,
    iterations: int | None = None,
    model: str | None = None,
    eoi: str | None = None,
    cvars: str | None = None,
    qvars: str | None = None,
    qcvar: str | None = None,
    stdz: str | None = None,
    wcp: int | None = None,
    disty: str | None = None,
    se: str | None = None,
    dbg_args: bool = False,
    help_: bool = False,
) -> MbaParameters:
    """
    Build parameters.
    
    Args:
        prefix: Prefix for output file names.
        data_table: Specify the data structure in a table of long format.
        chains: Specify the number of Markov chains.
        iterations: Specify the number of iterations per Markov chain.
        model: Specify the effects associated with explanatory variables.
        eoi: Identify effects of interest in the output.
        cvars: Identify categorical (qualitative) variables.
        qvars: Identify quantitative variables (or covariates).
        qcvar: Identify comparisons of interest between quantitative variables.
        stdz: Identify quantitative variables (or covariates) to be\
            standardized.
        wcp: Invoke within-chain parallelization to speed up runtime.
        disty: Specify the distribution for the response variable.
        se: Specify the column name that designates the standard error for the\
            response variable.
        dbg_args: Enable R to save the parameters in a file called\
            .MBA.dbg.AFNI.args for debugging purposes.
        help_: Show help message.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "MBA",
        "prefix": prefix,
        "data_table": data_table,
        "dbgArgs": dbg_args,
        "help": help_,
    }
    if chains is not None:
        params["chains"] = chains
    if iterations is not None:
        params["iterations"] = iterations
    if model is not None:
        params["model"] = model
    if eoi is not None:
        params["eoi"] = eoi
    if cvars is not None:
        params["cvars"] = cvars
    if qvars is not None:
        params["qvars"] = qvars
    if qcvar is not None:
        params["qcvar"] = qcvar
    if stdz is not None:
        params["stdz"] = stdz
    if wcp is not None:
        params["wcp"] = wcp
    if disty is not None:
        params["disty"] = disty
    if se is not None:
        params["se"] = se
    return params


def mba_cargs(
    params: MbaParameters,
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
    cargs.append("MBA")
    cargs.append(params.get("prefix"))
    if params.get("chains") is not None:
        cargs.extend([
            "-chains",
            str(params.get("chains"))
        ])
    if params.get("iterations") is not None:
        cargs.extend([
            "-iterations",
            str(params.get("iterations"))
        ])
    if params.get("model") is not None:
        cargs.extend([
            "-model",
            params.get("model")
        ])
    if params.get("eoi") is not None:
        cargs.extend([
            "-EOI",
            params.get("eoi")
        ])
    cargs.extend([
        "-dataTable",
        execution.input_file(params.get("data_table"))
    ])
    if params.get("cvars") is not None:
        cargs.extend([
            "-cVars",
            params.get("cvars")
        ])
    if params.get("qvars") is not None:
        cargs.extend([
            "-qVars",
            params.get("qvars")
        ])
    if params.get("qcvar") is not None:
        cargs.extend([
            "-qContr",
            params.get("qcvar")
        ])
    if params.get("stdz") is not None:
        cargs.extend([
            "-stdz",
            params.get("stdz")
        ])
    if params.get("wcp") is not None:
        cargs.extend([
            "-WCP",
            str(params.get("wcp"))
        ])
    if params.get("disty") is not None:
        cargs.extend([
            "-distY",
            params.get("disty")
        ])
    if params.get("se") is not None:
        cargs.extend([
            "-se",
            params.get("se")
        ])
    if params.get("dbgArgs"):
        cargs.append("-dbgArgs")
    if params.get("help"):
        cargs.append("-help")
    return cargs


def mba_outputs(
    params: MbaParameters,
    execution: Execution,
) -> MbaOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MbaOutputs(
        root=execution.output_file("."),
        output_txt=execution.output_file(params.get("prefix") + ".txt"),
        output_rdata=execution.output_file(params.get("prefix") + ".RData"),
        matrix_plot=execution.output_file(params.get("prefix") + "_matrixplot.png"),
    )
    return ret


def mba_execute(
    params: MbaParameters,
    execution: Execution,
) -> MbaOutputs:
    """
    Matrix-Based Analysis Program through Bayesian Multilevel Modeling.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MbaOutputs`).
    """
    params = execution.params(params)
    cargs = mba_cargs(params, execution)
    ret = mba_outputs(params, execution)
    execution.run(cargs)
    return ret


def mba(
    prefix: str,
    data_table: InputPathType,
    chains: int | None = None,
    iterations: int | None = None,
    model: str | None = None,
    eoi: str | None = None,
    cvars: str | None = None,
    qvars: str | None = None,
    qcvar: str | None = None,
    stdz: str | None = None,
    wcp: int | None = None,
    disty: str | None = None,
    se: str | None = None,
    dbg_args: bool = False,
    help_: bool = False,
    runner: Runner | None = None,
) -> MbaOutputs:
    """
    Matrix-Based Analysis Program through Bayesian Multilevel Modeling.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        prefix: Prefix for output file names.
        data_table: Specify the data structure in a table of long format.
        chains: Specify the number of Markov chains.
        iterations: Specify the number of iterations per Markov chain.
        model: Specify the effects associated with explanatory variables.
        eoi: Identify effects of interest in the output.
        cvars: Identify categorical (qualitative) variables.
        qvars: Identify quantitative variables (or covariates).
        qcvar: Identify comparisons of interest between quantitative variables.
        stdz: Identify quantitative variables (or covariates) to be\
            standardized.
        wcp: Invoke within-chain parallelization to speed up runtime.
        disty: Specify the distribution for the response variable.
        se: Specify the column name that designates the standard error for the\
            response variable.
        dbg_args: Enable R to save the parameters in a file called\
            .MBA.dbg.AFNI.args for debugging purposes.
        help_: Show help message.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MbaOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MBA_METADATA)
    params = mba_params(
        prefix=prefix,
        chains=chains,
        iterations=iterations,
        model=model,
        eoi=eoi,
        data_table=data_table,
        cvars=cvars,
        qvars=qvars,
        qcvar=qcvar,
        stdz=stdz,
        wcp=wcp,
        disty=disty,
        se=se,
        dbg_args=dbg_args,
        help_=help_,
    )
    return mba_execute(params, execution)


__all__ = [
    "MBA_METADATA",
    "MbaOutputs",
    "MbaParameters",
    "mba",
    "mba_params",
]
